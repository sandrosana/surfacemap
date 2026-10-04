import json
import networkx as nx
from networkx.readwrite import json_graph
from typing import Optional

def export_graph_json(G: nx.Graph, filename: str = "surface_graph.json") -> None:
    """Export the graph to a JSON file using node-link format."""
    data = json_graph.node_link_data(G)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def export_graph_html(G: nx.Graph, filename: str = "surface_graph.html") -> None:
    """Export the graph to a very basic HTML representation."""
    lines = ["<html>", "<body>", "<h1>Surface Graph</h1>", "<ul>"]
    for node in G.nodes:
        neighbours = ", ".join(str(n) for n in G.neighbors(node))
        lines.append(f"<li><strong>{node}</strong>: {neighbours}</li>")
    lines.extend(["</ul>", "</body>", "</html>"])
    with open(filename, "w") as f:
        f.write("\n".join(lines))
