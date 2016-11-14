#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import searching
from playing_field import PlayingField

def main(filename):
    field = PlayingField(filename)
    print("Start: " + str(field.findStartNode()))
    print(field)
    field.search(searching.bfs)

if __name__ == "__main__":
    main(sys.argv[1])
