import networkx as nx


def trios(pairs):
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            s = set(pairs[i]) | set(pairs[j])
            if len(s) == 3:
                for k in range(j + 1, len(pairs)):
                    s1 = s | set(pairs[k])
                    if len(s1) == 3:
                        yield list(s1)


def part_a(data):
    pairs = [tuple(x.split("-")) for x in data.lines()]
    return sum(any(x.startswith("t") for x in y) for y in trios(pairs))


def part_b(data):
    pairs = [tuple(x.split("-")) for x in data.lines()]
    G = nx.Graph()
    G.add_edges_from(pairs)
    cliques = list(nx.enumerate_all_cliques(G))
    m = max(cliques, key=lambda x: len(x))
    return ",".join(sorted(m))
