#!/usr/bin/env python
import sys
import argparse


variables = set()
domains = {}
columns = []


def main(word_list):
    initialize_variables(word_list)
    initialize_domains()
    initialize_columns(word_list)


def initialize_domains():
    """ Create an entry in domains for each letter with values from 0 to 9.
    """
    for variable in variables:
        domains[variable] = list(range(0, 10))


def initialize_variables(word_list):
    """ Build a set containing each letter once.
    """
    for word in word_list:
        for character in word:
            variables.add(character)


def initialize_columns(word_list):
    """
    """
    length = find_longest_word(word_list)

    # create each column as a list in columns
    for i in range(0, length + 1):
        columns.append([])

    for word in word_list:
        for char_index, char in enumerate(word[::-1]):
            columns[char_index].append(char)
    columns.reverse()


def find_longest_word(word_list):
    length = 0
    for word in word_list:
        new_length = len(word)
        if length < new_length:
            length = new_length
    return length


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
