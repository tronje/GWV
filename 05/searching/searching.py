# -*- coding: utf-8 -*-

import math
import time
from searching import heuristics
from playing_field import Path

"""Various search functions
"""

def bfs(pfield, start, goal='g', wall='x', info=False):
    """Breadth first search, starting at `start`, ending at `goal`.

    Params:
    -------
    pfield : PlayingField
        The PlayingField to be searched.
    start : Node
        Node object to start at
    goal : str
        The (length 1) string to end the search at
    wall : str
        String of length 1 that is treated as non-traversable
    """

    # set distance for our start node
    start.distance = 0

    # a list in python can be used just like a queue
    queue = [start]

    # count number of expansion operations and max queue size
    ops = 0
    max_len = 0

    while len(queue) > 0:
        if len(queue) > max_len:
            max_len = len(queue)

        # pop(0) is the same as dequeue
        current = queue.pop(0)

        # iterate over all neighbours
        for node in neighbours(current, pfield):
            # if it's a valid node...
            if node.distance == math.inf and node.value != wall:
                # ...set its parent
                node.parent = current
                # ...and distance
                node.distance = current.distance + 1

                # see if we found our goal
                if node.value == goal:
                    if info:
                        print("number of expansion operations: {}".format(ops))
                        print("max queue length: {}".format(max_len))
                        print()
                    return node
                else:
                    # same as enqueue
                    queue.append(node)
                    ops += 1

    raise ValueError("Goal '{}' not found in playing field!".format(goal))

def dfs(pfield, start, goal='g', wall='x', info=False):
    """Depth first search, starting at `start`, ending at `goal`.
    """

    start.distance = 0

    # a list in python can be used just like a stack
    stack = [start]

    # count number of expansion operations and max stack size
    ops = 0
    max_len = 0

    while len(stack) > 0:
        if len(stack) > max_len:
            max_len = len(stack)

        # note: pop() is the last element
        # as long as we use append() to add elements,
        # the stack behaviour is guaranteed
        current = stack.pop()

        # iterate over neighbours
        for node in neighbours(current, pfield):
            if node.distance == math.inf and node.value != wall:
                node.parent = current
                node.distance = current.distance + 1

                if node.value == goal:
                    if info:
                        print("number of expansion operations: {}".format(ops))
                        print("max stack size: {}".format(max_len))
                        print()
                    return node
                else:
                    # same as push()
                    stack.append(node)
                    ops += 1

    raise ValueError("Goal '{}' not found in pfield!".format(goal))

def astar(
        pfield,
        start,
        goal='g',
        wall='x',
        hfunc=heuristics.h_distance_portals,
        info=False):
    """A-star search, starting at `start`, ending at `goal`.
    """

    # set distance for our start node
    start.distance = 0

    # a list in python can be used just like a queue
    queue = [start]

    # count number of expansion operations and max queue length
    ops = 0
    max_len = 0

    # find the goal node to use with the heuristic function later
    gnode = pfield.find_node(goal)

    while len(queue) > 0:
        if len(queue) > max_len:
            max_len = len(queue)

        # pop(0) is the same as dequeue
        current = queue.pop(0)

        # iterate over all neighbours
        for node in neighbours(current, pfield):
            # if it's a valid node...
            if node.distance == math.inf and node.value != wall:
                # ...set its parent
                node.parent = current
                # ...and distance
                node.distance = current.distance + 1
                # ...and estimate the cost for the entire path,
                # if this node were in fact part of it.
                node.est_cost = node.distance + hfunc(pfield, node, gnode)

                # see if we found our goal
                if node.value == goal:
                    if info:
                        print("number of expansion operations: {}".format(ops))
                        print("max queue length: {}".format(max_len))
                        print()
                    return node
                else:
                    # p = Path(node, pfield)
                    # p.pretty()
                    # time.sleep(0.3)
                    # print("\033[1;J")
                    # same as enqueue
                    queue.append(node)
                    ops += 1

                    # sort by distance to simulate a priority queue
                    queue.sort(key=lambda x: x.est_cost)

    raise ValueError("Goal '{}' not found in playing field!".format(goal))


def neighbours(node, pfield, handle_portals=True):
    """All neighbours of a Node in a PlayingField.

    Params:
    -------
    node : Node
    pfield : PlayingField

    Returns:
    --------
    A list of all neighbours
    """

    ret = []
    env = pfield.env

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
                    ret += neighbours(field, pfield, handle_portals=False)

    return ret
