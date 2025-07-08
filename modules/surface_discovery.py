import json

def run_discovery(domain, output_file):
    print(f"[+] Starting surface discovery for: {domain}")
    results = {
        "domain": domain,
        "subdomains": [f"www.{domain}", f"mail.{domain}", f"vpn.{domain}"],
        "ips": ["192.0.2.1", "198.51.100.23"]
    }

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"[+] Discovery results saved to {output_file}")
