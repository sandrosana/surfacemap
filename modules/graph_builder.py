import networkx as nx
from typing import Dict, Any

def build_graph(data: Dict[str, Any]) -> nx.Graph:
    """Build a simple graph representing relationships between a domain,
    its subdomains and IP addresses.

    Parameters
    ----------
    data: dict
        Dictionary with keys ``domain``, ``subdomains`` and ``ips``.

    Returns
    -------
    networkx.Graph
        Generated graph with nodes and edges representing the surface.
    """
    G = nx.Graph()

    domain = data.get("domain")
    if not domain:
        return G

    G.add_node(domain, type="domain")

    subdomains = data.get("subdomains", [])
    ips = data.get("ips", [])

    for sub in subdomains:
        G.add_node(sub, type="subdomain")
        G.add_edge(domain, sub)

    for ip in ips:
        G.add_node(ip, type="ip")
        # Connect the domain to the IP address
        G.add_edge(domain, ip)
        # Connect each subdomain to the IP address as a simple heuristic
        for sub in subdomains:
            G.add_edge(sub, ip)

    return G
