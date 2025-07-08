import json
import os
from modules.graph_builder import build_graph
from modules.graph_export import export_graph_html, export_graph_json


def run_analysis(input_file: str, html=True, json_out=True):
    print(f"[+] Starting vulnerability graph generation from: {input_file}")

    if not os.path.exists(input_file):
        print(f"[!] Input file not found: {input_file}")
        return

    with open(input_file, "r") as f:
        data = json.load(f)

    G = build_graph(data)

    if html:
        export_graph_html(G, filename="surface_graph.html")
    if json_out:
        export_graph_json(G, filename="surface_graph.json")

    print("[+] Analysis complete. Output files: surface_graph.html, surface_graph.json")
