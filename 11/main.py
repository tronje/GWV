#!/usr/bin/env python
import sys
import argparse


variables = set()
domains = {}


def main(words):
    initialize_variables(words)
    initialize_full_domains()


def initialize_full_domains():
    for variable in variables:
        domains[variable] = list(range(0, 10))


def initialize_variables(word_list):
    for word in word_list:
        for character in word:
            variables.add(character)


def parse_args():
    # use argparse to parse command line arguments

    # initialise a parser
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
