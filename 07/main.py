#!/usr/bin/env python3

from arc_consistency import Node, Network, Constraint
from make_constraints import make_constraints

def _read_words(filename):
    wlist = []

    with open(filename, "r") as f:
        for line in f:
            # slice to -1 to remove trailing newline
            wlist.append(line[:-1])

    return wlist

def _make_network():
    wlist = _read_words("wordlist.txt")

    nodes = []

    nodes.append(Node(meta={'name': 'A1'}))
    nodes.append(Node(meta={'name': 'A2'}))
    nodes.append(Node(meta={'name': 'A3'}))
    nodes.append(Node(meta={'name': 'D1'}))
    nodes.append(Node(meta={'name': 'D2'}))
    nodes.append(Node(meta={'name': 'D3'}))
    # nodes.append(Node(meta={'position': (0, 0)}))
    # nodes.append(Node(meta={'position': (0, 1)}))
    # nodes.append(Node(meta={'position': (0, 2)}))
    # nodes.append(Node(meta={'position': (1, 0)}))
    # nodes.append(Node(meta={'position': (1, 1)}))
    # nodes.append(Node(meta={'position': (1, 2)}))
    # nodes.append(Node(meta={'position': (2, 0)}))
    # nodes.append(Node(meta={'position': (2, 1)}))
    # nodes.append(Node(meta={'position': (2, 2)}))

    # every node's domain contains all words
    for node in nodes:
        # pos = node.meta['position']
        for word in wlist:
            node.domain.add(word)
            # node.domain.add(word[pos[0]])
            # node.domain.add(word[pos[1]])

    nwork = Network(nodes)
    return nwork

def main():
    nwork = _make_network()
    make_constraints(nwork)
    nwork.gac()

    for node in nwork.nodes:
        print(node.meta['name'], node.domain)
    # for node in nwork.nodes:
    #     print(node)

if __name__ == "__main__":
    main()
