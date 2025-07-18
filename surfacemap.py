#!/usr/bin/env python3
import argparse
from modules.surface_discovery import run_discovery
from modules.surface_analyzer import run_analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SurfaceMap - External Attack Surface Assessment Tool")
    parser.add_argument("--analyze", action="store_true", help="Run vulnerability graph analysis on discovery results")
    parser.add_argument("--domain", help="Target domain to enumerate and assess")
    parser.add_argument("--output", default="surfacemap_output.json", help="Output file for results")
    args = parser.parse_args()

    if args.domain:
        run_discovery(args.domain, args.output)
    elif args.analyze:
        run_analysis(args.output)
    else:
        print("[!] Please provide a domain with --domain or use --analyze")
