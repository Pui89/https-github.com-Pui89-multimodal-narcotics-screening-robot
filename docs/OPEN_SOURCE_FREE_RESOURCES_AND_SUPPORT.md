# Free and Open-Source Tools, Funding, Compute and Hardware Support

This guide distinguishes resources that are free to use from competitive grants, credits, loans and donations. **No grant, cloud credit, equipment donation or company response is guaranteed.** Check the linked official program pages for current deadlines, country restrictions, legal-entity requirements and terms before applying. Program rules can change.

## Free software and tools

These tools have free/open-source options; always check each project's license, model/dataset terms, hardware requirements and third-party dependencies before commercial use.

- **ROS 2** — robotics middleware: https://docs.ros.org/
- **Gazebo** — robot and sensor simulation: https://gazebosim.org/
- **Webots** — robot simulation: https://cyberbotics.com/
- **OpenCV** — computer vision: https://opencv.org/
- **PyTorch** — deep learning: https://pytorch.org/
- **Hugging Face** — models, datasets and demos; usage/compute limits apply: https://huggingface.co/
- **Nav2** — ROS 2 navigation: https://nav2.org/
- **SLAM Toolbox** — mapping/localization: https://github.com/SteveMacenski/slam_toolbox
- **Open3D** — 3D data processing: https://www.open3d.org/
- **GitHub Actions** — CI minutes and artifact storage have plan-specific limits: https://github.com/features/actions
- **ONNX Runtime** — model inference: https://onnxruntime.ai/
- **MuJoCo** — physics simulation: https://mujoco.org/

Free software does not mean free physical hardware, unlimited cloud compute, unrestricted model weights, or a guarantee of commercial-use rights.

## Funding, compute and hardware-support leads

These are application routes, not confirmed awards. Tailor every request to the program's current eligibility rules.

| Organization / program | Possible support | Official route |
| --- | --- | --- |
| Thailand National Innovation Agency (NIA) | Eligible Thai innovation grants and commercialization support | https://www.nia.or.th/service/financial-support |
| depa Thailand | Digital startup / digital innovation funding calls | https://www.depa.or.th/th/startup and https://depa.or.th/th/funds |
| AMD University Program | Potential academic research hardware/software support; university eligibility may be required | https://www.amd.com/en/corporate/university-program.html |
| Seeed Studio Academic Support | Possible research collaboration, components or support for eligible applicants | https://academic.seeed.cc/ |
| Stereolabs | Ask about camera loan, research pricing or technical evaluation; donation is not promised | https://www.stereolabs.com/ |
| NVIDIA Inception | Free program membership and potential partner benefits; not a guaranteed GPU donation | https://www.nvidia.com/en-us/startups/ |
| AWS Activate | Potential AWS cloud credits for eligible startups; credits are not cash or hardware | https://aws.amazon.com/startups/ |
| Google for Startups Cloud Program | Potential cloud credits for eligible startups; tier and eligibility restrictions apply | https://cloud.google.com/startup/ |
| Hugging Face community GPU grants | Competitive compute support for qualifying public demos/research | https://github.com/huggingface/skills/blob/main/skills/huggingface-spaces/references/grants.md |
| Qualcomm AI Program for Innovators (APAC) | Cohort-specific hardware/grant support; check eligible countries and current application window | https://www.qualcomm.com/ai-program-for-innovators/apac |
| Open Robotics / ROS community | Open-source tools, community guidance and ecosystem collaboration, not a general cash grant | https://www.openrobotics.org/contact |

### Contacts previously identified — verify before sending

- AMD University Program: `aup@amd.com` — check the official program page for current contact instructions.
- Seeed Studio: `bp@seeed.cc` and `seeed_apac@seeed.cc` — verify current regional/program contacts on Seeed's official site.
- Stereolabs: `support@stereolabs.com` — ask to be routed to research/business development.
- Google Cloud startup support: `cloudstartupsupport@google.com` — confirm that this address is still supported and that your application qualifies.
- Thailand NIA and depa: use the contact details and application instructions displayed on their official sites, as program-specific contacts can change.
- Qualcomm: use the contact channel on the current APAC program page; past cohorts may be closed or country-restricted.

Do not send sensitive personal documents or bank details to an unverified address. Never pay a fee just to be considered for an alleged grant without independently verifying the program.

## Recommended no-hardware-first workflow

1. Build and run the project on the computer you already have.
2. Use simulation and public datasets where their licenses permit the intended use.
3. Add repeatable tests, raw benchmark outputs, system requirements and known limitations.
4. Publish a short demonstration and a one-page hardware request with exact quantities and specifications.
5. Ask for a loan or evaluation kit before requesting a permanent donation.
6. Apply for funding only after checking whether individuals, Thai-registered businesses or university partners are eligible.
7. Keep a support ledger documenting applications, deadlines, contacts, status, promised benefits and any restrictions.

## 2026–2028 support plan

- **2026:** Simulation-first proof of concept, software tests, documented benchmarks, applications to currently open programs.
- **2027:** Use measured results to seek academic collaborators, hardware loans, field-test partners and eligible grant rounds.
- **2028:** Pursue larger grants and commercial pilots only after safety, reliability, legal compliance and field performance are independently evaluated.

## Evidence and integrity rules

- Label each result as a target, simulation result, lab result or field result.
- Do not claim a grant, partnership, hardware donation, certification or benchmark success until it is confirmed and documented.
- Record license obligations for code, models, datasets and generated artifacts.
- Do not represent cloud credits as cash or as physical equipment.

## Project-specific priority: Multimodal Screening Robot

### First free stack to try
- ROS 2 + Gazebo/Webots for safe robot and inspection-workflow simulation.
- OpenCV and PyTorch for general visual inspection and anomaly-detection research.
- Anomalib for visual anomaly-detection experiments: https://github.com/open-edge-platform/anomalib
- Open3D for external surface/scene geometry.
- GitHub Actions for tests, audit logs and reproducible evaluations.

### Best-fit support requests
1. NIA / depa: ask about eligible AI, inspection, safety or digital innovation funding.
2. AMD University Program: ask about research computing through an eligible academic partner.
3. Seeed Studio: request non-invasive camera, depth-sensor or edge-computing evaluation hardware.
4. NVIDIA Inception / AWS Activate / Google for Startups: investigate eligible startup benefits and compute credits.
5. University labs and authorized inspection organizations: seek a formal research/ethics and evaluation partnership before real-world deployment.

### Safety, privacy and claims boundary
This project should be described as decision support for authorized, non-invasive external-object/scene screening. Ordinary cameras, thermal/NIR, depth sensors, LiDAR and AI models cannot reliably establish the chemical identity of a concealed substance or determine whether a person has ingested drugs. Do not use a model output alone to accuse, detain, search or otherwise penalize a person. Keep a trained human reviewer in the loop, show uncertainty, log evidence and provide a clear abstain/unknown outcome. Follow applicable privacy, security, evidence-handling and local legal requirements.

### Suggested measurable evidence
Evaluate false-positive and false-negative rates on legally obtained, appropriately governed test data; calibration and abstention quality; robustness to lighting/occlusion/sensor failure; processing latency; human-review agreement; privacy controls; and audit-log completeness. Avoid publishing sensitive operational detection recipes or claiming chemical identification without a validated instrument and independent evidence.
