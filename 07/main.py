#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _read_words(filename):
    wlist = []

    with open(filename, "r") as f:
        for line in f:
            # slice to -1 to remove trailing newline
            wlist.append(line[:-1])

    return wlist

def main():
    print(_read_words("wordlist.txt"))

if __name__ == "__main__":
    main()
