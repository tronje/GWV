#!/usr/bin/env python3
import sys
import argparse
from csp import Network, Variable, Constraint, UnaryConstraint


def make_network(words):
    chars = set()
    variables = []
    domain = set(range(10))

    # find all chars
    for word in words:
        for char in word:
            chars.add(char)

    # create a Variable for each char
    for char in chars:
        # it's gonna need a meta-dictionary,
        # which will contain the char...
        meta = {'char': char,
                'leading': False,
                'surrogate': False,
                'overflow': False,
                'sum': False}

        # and the positions in the words it's contained in
        for word in words:
            meta[word] = []
            if char in word:
                for i in range(len(word)):
                    if word[i] == char:
                        meta[word].append(i)

            # remember if the char is the same as the last element
            # of the word. Since the word is reversed, it would be the first
            # element, and thus cannot be zero. We remember this with the
            # 'leading' key.
            if char == word[-1]:
                meta['leading'] = True

            if char in words[-1]:
                meta['sum'] = True

        # build the variable
        variables.append(
            Variable(
                # need a copy here! can't have all domains
                # be the same list!
                domain=domain.copy(),
                meta=meta.copy()
            )
        )

    # surrogate variables for sums of variables above the sum line
    meta = {'char': None,
            'leading': False,
            'surrogate': True,
            'overflow': False,
            'sum': False}
    domain = set(range((len(words) - 1) * 9))

    for i in range(len(words[-1])):
        meta['column'] = i
        variables.append(
            Variable(
                domain=domain.copy(),
                meta=meta.copy()
            )
        )

    # variables that account for addition overflow
    meta = {'char': None,
            'leading': False,
            'surrogate': False,
            'overflow': True,
            'sum': False}
    domain = set(range(3))

    for i in range(len(words[-1])):
        meta['column'] = i
        variables.append(
            Variable(
                domain=domain.copy(),
                meta=meta.copy()
            )
        )

    # create a basic network with these variables
    return Network(variables)


def make_constraints(nwork, words):
    # unary constraints
    for variable in nwork.variables:
        if variable.meta['leading']:
            # if it's the first char in a word, it can't be 0
            # as one of the conditions is no leading zeros!
            nwork.unary_constraints.append(
                UnaryConstraint(variable, lambda x: x != 0)
            )

    # 'regular'/binary constraints
    constraints = []

    for variable in nwork.variables:
        if variable.meta['surrogate']:
            other_var = nwork.get_variable(words[-1], variable.meta['column'])
            constraints.append(
                Constraint(
                    [other_var, variable],
                    lambda x, y: x == y
                )
            )

        # no variable may have the same value as a different variable
        if variable.meta['char'] is not None:
            for other_var in nwork.variables:
                if other_var is variable:
                    continue

                constraints.append(
                    Constraint(
                        [variable, other_var],
                        lambda x, y: x != y
                    )
                )

    # add constraints to network
    nwork.constraints += constraints


def main(words):
    # reverse words to normalize indices
    words = [word[::-1] for word in words]

    nwork = make_network(words)
    make_constraints(nwork, words)
    nwork.gac()

    for variable in nwork.variables:
        # print(variable.meta['char'], variable.domain)
        print(variable)


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
