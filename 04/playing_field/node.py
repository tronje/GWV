# -*- coding: utf-8 -*-

import math

class Node(object):
    """A node in a graph, which has a value,
    a distance (from some start node) and a parent.
    Intended to be used with, i.e., breadth-first-search.
    """

    def __init__(self, value, coords, distance=math.inf, parent=None):
        """Initialize a Node.

        Params:
        -------
        value : object
            The value saved by this node.
        coords : (int, int)
            the coordinates of this Node in the PlayingField
        distance : int
            A variable to hold a distance to be assigned by a search algorithm.
            Default is infinity.
        parent : Node
            A variable to hold a parent to be assigned by a search algorithm.
        """

        self.value = value
        self.coords = coords
        self.distance = distance
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def isBlocked(self):
        '''
        :param xy:
        :return: boolean
        '''
        return self.value == 'x'

    def isStart(self):
        '''
        :param xy: Node
        :return: boolean
        '''
        return self.value == 's'

    def isTarget(self):
        '''
        :param xy:
        :return: boolean
        '''
        return self.value == 'g'

    def isPortal(self):
        '''
        :param xy:
        :return: None/xy-target
        '''
        return self.value.isdigit()

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

