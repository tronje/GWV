# -*- coding: utf-8 -*-

import math
from searching import heuristics

"""Various search functions
"""

def bfs(pfield, start, goal='g', wall='x'):
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

    while len(queue) > 0:
        # pop(0) is the same as dequeue
        current = queue.pop(0)

        # iterate over all neighbours
        for node in neighboursOf(current, pfield):
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

    raise ValueError("Goal '{}' not found in playing field!".format(goal))

def dfs(pfield, start, goal='g', wall='x'):
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
        for node in neighboursOf(current, pfield):
            if node.distance == math.inf and node.value != wall:
                node.parent = current
                node.distance = current.distance + 1

                if node.value == goal:
                    return node
                else:
                    # same as push()
                    stack.append(node)

    raise ValueError("Goal '{}' not found in pfield!".format(goal))

def astar(pfield, start, goal='g', wall='x', hfunc=heuristics.h_distance):
    """A-star search, starting at `start`, ending at `goal`.
    """

    # set distance for our start node
    start.distance = 0

    # a list in python can be used just like a queue
    queue = [start]

    while len(queue) > 0:
        # pop(0) is the same as dequeue
        current = queue.pop(0)

        # iterate over all neighbours
        for node in neighboursOf(current, pfield):
            # if it's a valid node...
            if node.distance == math.inf and node.value != wall:
                # ...set its parent
                node.parent = current
                # ...and distance
                node.distance = current.distance + 1
                # ...and estimate the cost for the entire path,
                # if this node were in fact part of it.
                node.est_cost = node.distance + hfunc(pfield, node)

                # see if we found our goal
                if node.value == goal:
                    return node
                else:
                    # same as enqueue
                    queue.append(node)

                    # sort by distance to simulate a priority queue
                    queue.sort(key=lambda x: x.est_cost)

    raise ValueError("Goal '{}' not found in playing field!".format(goal))


def neighboursOf(node, pfield, handle_portals=True):
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
                    ret += neighboursOf(field, pfield, handle_portals=False)

    return ret
