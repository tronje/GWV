# -*- coding: utf-8 -*-

import math

class Node(object):
    """A node in a PlayingField, which has a value, coordinates,
    a distance (from some start node) and a parent.
    """

    def __init__(
            self,
            value,
            coords,
            distance=math.inf,
            est_cost=math.inf,
            parent=None):
        """Initialize a Node.

        Params:
        -------
        value : object
            The value saved by this node.
        coords : (int, int)
            the coordinates of this Node in the PlayingField as a tuple
        distance : int
            A variable to hold a distance to be assigned by a search algorithm.
            Default is infinity.
        est_cost : int
            Holds the estimated distance; useful e.g. for A*.
        parent : Node
            A variable to hold a parent to be assigned by a search algorithm.
        """

        self.value = value
        self.coords = coords
        self.distance = distance
        self.est_cost = est_cost
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        """Equality check; only value and coords matter here.
        """

        # always check the type first!
        return type(self) == type(other)\
                and (self.value == other.value)\
                and (self.coords == other.coords)

    @property
    def x(self):
        """The x-coordinate"""
        return self.coords[0]

    @property
    def y(self):
        """The y-coordinate"""
        return self.coords[1]

    def is_portal(self):
        """Return True if this Node is a portal, False otherwise.
        Portals are Nodes with numeric values, as opposed to
        alphabetical characters.
        """

        return self.value.isdigit()
