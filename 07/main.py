#!/usr/bin/env python3

from arc_consistency import Node, Network

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

    nodes.append(Node(meta={'position': (0,0)}))
    nodes.append(Node(meta={'position': (1,0)}))
    nodes.append(Node(meta={'position': (2,0)}))
    nodes.append(Node(meta={'position': (0,1)}))
    nodes.append(Node(meta={'position': (1,1)}))
    nodes.append(Node(meta={'position': (2,1)}))
    nodes.append(Node(meta={'position': (0,2)}))
    nodes.append(Node(meta={'position': (1,2)}))
    nodes.append(Node(meta={'position': (2,2)}))

    for node in nodes:
        # grab our position
        pos = node.meta['position']

        # for every word, add the letter at the corresponding
        # place to the domain; keep in mind that the domain
        # is a set and cannot contain duplicates
        for w in wlist:
            node.domain.add(w[pos[0]])
            node.domain.add(w[pos[1]])

    nwork = Network(nodes)
    return nwork

def main():
    print(_make_network())
    # _make_network()

if __name__ == "__main__":
    main()
