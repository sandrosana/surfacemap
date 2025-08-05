import json
from pathlib import Path


def run_discovery(domain, output_file):
    print(f"[+] Starting surface discovery for: {domain}")
    results = {
        "domain": domain,
        "subdomains": [f"www.{domain}", f"mail.{domain}", f"vpn.{domain}"],
        "ips": ["192.0.2.1", "198.51.100.23"]
    }

    base_dir = Path.cwd().resolve()
    output_path = Path(output_file).expanduser().resolve()
    if not output_path.is_relative_to(base_dir):
        print(f"[!] Output path escapes working directory: {output_file}")
        return

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"[+] Discovery results saved to {output_path}")
