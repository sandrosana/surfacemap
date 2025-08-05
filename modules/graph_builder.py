import networkx as nx


def build_graph(data: dict) -> nx.Graph:
    """Build a simple graph from discovery data."""
    G = nx.Graph()
    domain = data.get("domain")
    if not domain:
        return G
    G.add_node(domain, type="domain")
    for sub in data.get("subdomains", []):
        G.add_edge(domain, sub, type="subdomain")
    for ip in data.get("ips", []):
        G.add_edge(domain, ip, type="ip")
    return G
