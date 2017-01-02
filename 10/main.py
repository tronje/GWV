#!/usr/bin/env python
import sys
import argparse

def parse_args():
    # use argparse to parse command line arguments

    ## init a parser
    parser = argparse.ArgumentParser(description='A simple PoS-Tagger')

    ## declare all arguments
    parser.add_argument('filenames', nargs='*', help='the file to search through')

    ## gotta parse 'em all
    args = parser.parse_args()
    return args

def readfiles(filesnames):
    words = []
    for name in filesnames:
        with open(name, "r") as f:
            words.extend(f.readlines())
    return words

def main(filenames):
    words = readfiles(filenames)

if __name__=="__main__":
    args = parse_args()
    exit_status = main(args.filenames)

    # exit with a 0, which is nice
    sys.exit(exit_status)
