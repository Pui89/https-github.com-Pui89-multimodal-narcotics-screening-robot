from narcotics_platform.evidence_graph import EvidenceGraph

def test_evidence_graph_has_stable_digest():
    graph = EvidenceGraph('evt-1')
    graph.add_node('rgb-1','sensor',modality='rgb')
    graph.add_node('obs-1','observation',label='unknown_substance')
    graph.link('rgb-1','supports','obs-1')
    assert graph.digest() == graph.digest()
    assert len(graph.digest()) == 64
