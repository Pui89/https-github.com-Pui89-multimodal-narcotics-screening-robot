import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from e2e_screening.workflow import screen_case, verify_report
ROOT = Path(__file__).resolve().parents[1]
def sample(): return json.loads((ROOT/"examples/synthetic_screening_case.json").read_text())
class ScreeningE2ETests(unittest.TestCase):
    def test_sample_requires_human_review_and_no_enforcement(self):
        r=screen_case(sample()); self.assertEqual(r["status"],"HUMAN_REVIEW_FLAG")
        self.assertTrue(r["human_review_required"]); self.assertFalse(r["automated_enforcement_decision"])
        self.assertFalse(r["substance_presence_confirmed"]); self.assertTrue(verify_report(r))
    def test_insufficient_modalities_abstains(self):
        c=sample(); c["observations"]=c["observations"][:1]
        self.assertEqual(screen_case(c)["status"],"ABSTAIN_INSUFFICIENT_EVIDENCE")
    def test_low_quality_rejected(self):
        c=sample(); c["observations"][0]["quality_score"]=0.1
        self.assertIn("LOW_QUALITY",[x["reason"] for x in screen_case(c)["rejected_evidence"]])
    def test_ood_rejected(self):
        c=sample(); c["observations"][0]["ood_score"]=0.99
        self.assertIn("OUT_OF_DISTRIBUTION",[x["reason"] for x in screen_case(c)["rejected_evidence"]])
    def test_disagreement_escalates(self):
        c=sample(); c["observations"][0]["screening_score"]=0.05; c["observations"][1]["screening_score"]=0.99
        self.assertEqual(screen_case(c)["status"],"HUMAN_REVIEW_CONFLICTING_EVIDENCE")
    def test_person_screening_is_rejected(self):
        c=sample(); c["subject_type"]="person"
        with self.assertRaises(ValueError): screen_case(c)
    def test_duplicate_modality_rejected(self):
        c=sample(); c["observations"].append(dict(c["observations"][0]))
        with self.assertRaises(ValueError): screen_case(c)
    def test_tampering_detected(self):
        r=screen_case(sample()); r["status"]="CLEAR"
        self.assertFalse(verify_report(r))
    def test_invalid_score_rejected(self):
        c=sample(); c["observations"][0]["screening_score"]=float("nan")
        with self.assertRaises(ValueError): screen_case(c)
    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"report.json"
            subprocess.run([sys.executable,"-m","e2e_screening.workflow","--input",str(ROOT/"examples/synthetic_screening_case.json"),"--output",str(out)],check=True,cwd=ROOT,capture_output=True,text=True)
            self.assertTrue(verify_report(json.loads(out.read_text())))
if __name__=="__main__": unittest.main()
