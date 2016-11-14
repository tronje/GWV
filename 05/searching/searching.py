#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""Various search functions
"""

def bfs(env, start, goal='g', wall='x'):
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
    wall : str
        String of length 1 that is treated as non-traversable
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
            if node.distance == math.inf and node.value != wall:
                # ...set its parent
                node.parent = current
                # ...and distance
                node.distance = current.distance + 1

                # see if we found our goal
                if node.value == goal:
                    return node
                else:
                    # same as enqueue
                    queue.append(node)

    raise ValueError("Goal '{}' not found in env!".format(goal))

def dfs(env, start, goal='g', wall='x'):
    """Depth first search, starting at `start`, ending at `goal`.
    """

    start.distance = 0

    # a list in python can be used just like a stack
    stack = [start]

    while len(stack) > 0:
        # note: pop() is the last element
        # as long as we use append() to add elements,
        # the stack behaviour is guaranteed
        current = stack.pop()
        
        # iterate over neighbours
        for node in neighboursOf(current, env):
            if node.distance == math.inf and node.value != wall:
                node.parent = current
                node.distance = current.distance + 1

                if node.value == goal:
                    return node
                else:
                    # same as push()
                    stack.append(node)

    raise ValueError("Goal '{}' not found in env!".format(goal))

def astar(env, start, goal='g', wall='x'):
    """A-star search, starting at `start`, ending at `goal`.
    """

    # TODO
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

    # up
    ret.append(env[node.x][node.y + 1])

    # right
    ret.append(env[node.x + 1][node.y])

    # down
    ret.append(env[node.x][node.y - 1])

    # left
    ret.append(env[node.x - 1][node.y])

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
