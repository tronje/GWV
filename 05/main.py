#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import searching
import argparse
from playing_field import PlayingField

def main(args):
    """Entry point to the tool.
    
    Params:
    =======
    args : Namespace
        A namespace containing the arguments.
        Can theoretically be any other object providing
        the expected attributes, but is easily created
        using argparse.

        Expected attributes:
        --------------------
        filename : str
        strategy : str
        info     : bool
        progress : bool
    """

    # init a playing field, taking care to give
    # a nice error message if the file can't be found.
    try:
        pfield = PlayingField(args.filename)
    except FileNotFoundError:
        sys.stderr.write(
            "The file you specified ('{}') does not exist!\n"
            .format(args.filename)
        )
        sys.exit(1)

    # grab our search function from the searches dictionary
    # provided by the searching module
    sfunc = searching.searches[args.strategy]

    print("Start: " + str(pfield.find_start_node()))
    print("Using search strategy '{}'\n".format(sfunc.__name__))

    # print the initial playing field only if not printing progess
    # (doesn't matter much, but you just can't see it if progress is on)
    if not args.progress:
        print(pfield)

    # grab the time
    delta_t = time.process_time()

    # search through the playing field
    path = pfield.search(sfunc, info=args.info, progress=args.progress)

    # grab the time again, subtracting the time from before
    # to get the time taken
    delta_t = time.process_time() - delta_t

    # print some stuff and we're done
    print("Path found with length {}:".format(len(path)))
    path.pretty()
    print("time taken: {}s".format(delta_t))

if __name__ == "__main__":
    # use argparse to parse command line arguments

    ## init a parser
    parser = argparse.ArgumentParser(description='a little path search tool for uni')

    ## declare all arguments
    parser.add_argument('filename', help='the file to search through')
    parser.add_argument('strategy', choices=list(searching.searches.keys()), help='the search strategy to use')
    parser.add_argument('-i', '--info', action='store_true', help='print some algorithm stats')
    parser.add_argument('-p', '--progress', action='store_true', help='show algorithm progress')

    ## parse 'em
    args = parser.parse_args()

    ## pass them on to main to do its thing
    main(args)

    # exit with a 0, which is nice
    sys.exit(0)
