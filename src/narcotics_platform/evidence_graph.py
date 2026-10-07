from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from typing import Any

@dataclass
class EvidenceGraph:
    event_id: str
    nodes: dict[str, dict[str, Any]] = field(default_factory=dict)
    edges: list[dict[str, str]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def add_node(self, node_id: str, node_type: str, **attributes: Any) -> None:
        self.nodes[node_id] = {"type": node_type, **attributes}

    def link(self, source: str, relation: str, target: str) -> None:
        self.edges.append({"source": source, "relation": relation, "target": target})

    def digest(self) -> str:
        payload = {"event_id": self.event_id, "created_at": self.created_at, "nodes": self.nodes, "edges": self.edges}
        return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    def export(self) -> dict[str, Any]:
        return {"event_id": self.event_id, "created_at": self.created_at, "nodes": self.nodes, "edges": self.edges, "integrity_sha256": self.digest()}