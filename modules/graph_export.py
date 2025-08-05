import json
from pathlib import Path
import networkx as nx
from networkx.readwrite import json_graph


def _safe_path(filename: str) -> Path:
    base_dir = Path.cwd().resolve()
    path = Path(filename).expanduser().resolve()
    if not path.is_relative_to(base_dir):
        raise ValueError("Output path escapes working directory")
    return path


def export_graph_json(G: nx.Graph, filename: str = "surface_graph.json") -> None:
    path = _safe_path(filename)
    data = json_graph.node_link_data(G)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_graph_html(G: nx.Graph, filename: str = "surface_graph.html") -> None:
    path = _safe_path(filename)
    data = json.dumps(json_graph.node_link_data(G), indent=2)
    html = f"<html><body><pre>{data}</pre></body></html>"
    with path.open("w", encoding="utf-8") as f:
        f.write(html)
