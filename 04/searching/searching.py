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
        shall contain Node objects
    start : Node
        Node object to start at
    goal : str
        The (length 1) string to end the search at
    """

    # set distance for our start node
    start.distance = 0

    # a list in python can be used lust like a queue
    queue = [start]

    while len(queue) > 0:
        # pop(0) is the same as dequeue
        current = queue.pop(0)

        # iterate over all neighbours
        for node in neighboursOf(current, env):
            # if it's a valid node...
            if node.distance == math.inf and node.value != 'x':
                # ...set its parent
                node.parent = current
                # ...and distance
                node.distance = current.distance + 1

                # see if we found our goal
                if node.value == goal:
                    return node
                else:
                    queue.append(node)

    raise ValueError("Goal '{}' not found in env!".format(goal))

def dfs(env, start, goal='g'):
    """Depth first search, starting at `start`, ending at `goal`.
    """

    pass

def neighboursOf(node, env, handle_portals=True):
    """All neighbours of a Node in an Environment

    Params:
    -------
    node : Node
    env : List

    Returns:
    --------
    A list of all neighbours
    """

    ret = []
    ret.append(env[node.x + 1][node.y])
    ret.append(env[node.x - 1][node.y])
    ret.append(env[node.x][node.y + 1])
    ret.append(env[node.x][node.y - 1])

    # handle portals
    if handle_portals and node.value.isdigit():
        for line in env:
            for field in line:
                if (field.value == node.value
                        and field.coords != node.coords):
                    # append to our neighbours the neighbours
                    # of the other portal, but without handling
                    # portals again to avoid infinite recursion
                    ret += neighboursOf(field, env, handle_portals=False)

    return ret
