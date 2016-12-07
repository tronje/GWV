#!/usr/bin/env python3

from arc_consistency import Variable, Network, Constraint
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

    variables = []

    variables.append(Variable(domain=set(wlist), meta={'name': 'A1'}))
    variables.append(Variable(domain=set(wlist), meta={'name': 'A2'}))
    variables.append(Variable(domain=set(wlist), meta={'name': 'A3'}))
    variables.append(Variable(domain=set(wlist), meta={'name': 'D1'}))
    variables.append(Variable(domain=set(wlist), meta={'name': 'D2'}))
    variables.append(Variable(domain=set(wlist), meta={'name': 'D3'}))

    nwork = Network(variables)
    return nwork

def main():
    nwork = _make_network()
    make_constraints(nwork)
    nwork.gac()

    for variable in nwork.variables:
        print(variable.meta['name'], variable.domain)
        # print(variable)

if __name__ == "__main__":
    main()
