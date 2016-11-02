#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # print, to see if it worked
    env = read_env()
    print_env(env)

def read_env():
    # our virtual environment
    env = []

    # open file
    with open("blatt3_environment.txt", "r") as f:
        # list-ify each line in the file and add to env
        for line in f:
            env.append(list(line))

    # remove newlines, we don't need 'em
    for elem in env:
        elem.remove('\n')

    return env

def print_env(env):
    for line in env:
        for char in line:
            print(char, end="")
        print("")

if __name__ == '__main__':
    main()
