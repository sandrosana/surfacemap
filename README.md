# SurfaceMap

**SurfaceMap** is a modular tool for automated External Attack Surface Assessment (EASM), integrating discovery, vulnerability scanning, and interactive graphing.

## Features

- Domain & subdomain enumeration
- IP resolution
- CVE enrichment (coming soon)
- Visual graph generation (via VulnGraph)
- Risk scoring (coming soon)

## Installation

```bash
git clone https://github.com/sandrosana/surfacemap.git
cd surfacemap
pip install -r requirements.txt
```

## Usage

### Discovery Phase

```bash
python3 surfacemap.py --domain example.com --output results.json
```

### Graph Analysis Phase

```bash
python3 surfacemap.py --analyze --output results.json
```

## Output

- `results.json`: raw discovered assets
- `surface_graph.html`: interactive graph view
- `surface_graph.json`: graph data for API integration

## Roadmap

- Integration with cve-scanner
- Integration with osint-toolbox
- Exploit matcher & pathfinder modules
