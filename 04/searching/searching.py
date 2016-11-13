#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""Various search functions
"""

def bfs(env, start, goal='g'):
    """Breadth first search, starting at `start`, ending at `goal`.

    Params:
    -------
    env : list
        2-D list representing the PlayingField to be searched
    start : (int, int)
        x,y coordinates of the start node
    goal : str
        The (length 1) string to end the search at
    """
    start.distance = 0
    queue = [start]

    while len(queue) > 0:
        current = queue.pop(0)
        for node in neighboursOf(current, env):
            if node.distance == math.inf and node.value != 'x':
                node.parent = current
                node.distance = current.distance + 1
                if node.value == 'g':
                    return node
                else:
                    queue.append(node)
    return queue

def neighboursOf(node, env):
    """All neighbours of a Node in an Environment

    Params:
    -------
    node : Node
    env : List

    """
    x,y = node.coords
    ret = []
    ret.append(env[x+1][y])
    ret.append(env[x-1][y])
    ret.append(env[x][y+1])
    ret.append(env[x][y-1])
    return ret
