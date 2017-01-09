#!/usr/bin/env python
import sys
import argparse
from parser import *


def main(filenames, words):
    import_tagged_files(filenames)
    if words:
        last_tag = '$.'
        for word in words:
            last_tag = find_tag_for_word(word, last_tag)
            print(word+'\t'+last_tag)
            print('')


def find_tag_for_word(word, last_tag):
    tags = find_all_tags_for_word(word)

    most_used = (None, 0)
    for tag, count in tags:
        if count > most_used[1]:
            most_used = (tag, count)
    return most_used[0]


def find_all_tags_for_word(word):
    tags = []
    for tag, words in emission_count.items():
        for tagged_word, count in words.items():
            if word == tagged_word:
                tags.append((tag, count))
    return tags


def find_largest(arr):
    largest = (None, 0)
    for item, num in arr:
        if num > largest[1]:
            largest = (item, num)
    return largest


def find_parents(tag):
    parents = []
    for parent_tag, tags in transition_count.items():
        for current_tag, count in tags:
            if tag == current_tag:
                parents.append((parent_tag, count))
    return parents


def parse_args():
    # use argparse to parse command line arguments

    # init a parser
    parser = argparse.ArgumentParser(description='A simple PoS-Tagger')

    # declare all arguments
    parser.add_argument(
        '-f',
        nargs='+',
        help='the files to search through'
    )
    parser.add_argument(
        '-w',
        nargs='+',
        help='produce tags for given words'
    )

    # gotta parse 'em all
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    if args.f is None or args.w is None:
        print("Invalid arguments, use '-h' flag for help!")
        exit(1)
    exit_status = main(args.f, args.w)

    # exit with a 0, which is nice
    sys.exit(exit_status)
