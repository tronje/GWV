#!/usr/bin/env python
import sys
import argparse


def main(words):
    pass


def parse_args():
    # use argparse to parse command line arguments

    # init a parser
    parser = argparse.ArgumentParser(
        description='Cryptoarithmetic Puzzle Solver'
    )

    # declare all arguments
    parser.add_argument(
        'words',
        nargs='+',
        help='2-5 words; lined up to the right'
    )

    # gotta parse 'em all
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    if args.words is None:
        print("Invalid arguments, use '-h' flag for help!")
        exit(1)
    elif len(args.words) < 2 or len(args.words) > 5:
        print("Invalid number of words, please supply 2-5 words!")
    exit_status = main(args.words)

    # exit with a 0, which is nice
    sys.exit(exit_status)
