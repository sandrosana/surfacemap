# SurfaceMap

**SurfaceMap** is a modular tool for automated External Attack Surface Assessment (EASM), integrating discovery, vulnerability scanning, and interactive graphing.

## Features

- Domain & subdomain enumeration
- IP resolution
- CVE enrichment
- Visual graph generation
- Risk scoring (coming soon)

## Usage

```bash
python3 surfacemap.py --domain example.com --output results.json
```

## Roadmap

- Integration with `cve-scanner`
- Visual graph from `vulngraph`
- OSINT plugins (Shodan, WHOIS, ASN)
