import json
from pathlib import Path
from modules.graph_builder import build_graph
from modules.graph_export import export_graph_html, export_graph_json


def run_analysis(input_file: str, html=True, json_out=True):
    print(f"[+] Starting vulnerability graph generation from: {input_file}")

    base_dir = Path.cwd().resolve()
    input_path = Path(input_file).expanduser().resolve()
    if not input_path.is_relative_to(base_dir) or not input_path.exists():
        print(f"[!] Input file not found or outside working directory: {input_file}")
        return

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    G = build_graph(data)

    if html:
        export_graph_html(G, filename="surface_graph.html")
    if json_out:
        export_graph_json(G, filename="surface_graph.json")

    print("[+] Analysis complete. Output files: surface_graph.html, surface_graph.json")
