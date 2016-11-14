#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import searching
from playing_field import PlayingField

def main(filename, sfunc):
    field = PlayingField(filename)
    print("Start: " + str(field.findStartNode()))
    print(field)
    field.search(sfunc)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./main.py <filename> <search-strategy>")
        sys.exit(1)

    try:
        sfunc = searching.searches[sys.argv[2]]
    except KeyError:
        print("search strategy '{}' not supported!".format(sys.argv[2]))

    main(sys.argv[1], sfunc)
    sys.exit(0)
