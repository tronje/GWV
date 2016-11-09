#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Node(object):
    """A node in a graph, which has a value,
    a distance (from some start node) and a parent.
    Intended to be used with, i.e., breadth-first-search.
    """

    def __init__(self, value, distance=math.inf, parent=None):
        """Initialize a Node.

        Params:
        -------
        value : object
            The value saved by this node.
        distance : int
            A variable to hold a distance to be assigned by a search algorithm.
            Default is infinity.
        parent : Node
            A variable to hold a parent to be assigned by a search algorithm.
        """

        self.value = value
        self.distance = distance
        self.parent = parent

    def __str__(self):
        return str(self.value)

class PlayingField(object):
    """Represents a playing field, which is read
    from a file and stored in a 2d-list.
    Can be printed and (TODO) searched through.
    """

    def __init__(self, filename):
        """Initialize a playing field.

        Params:
        -------
        filename : str
            The name of the file from which to read
            the playing field.
        """

        # name of the file to use
        self._filename = filename

        # our virtual environment
        self._environment = []

        # read env from the file
        self._read_env()

    def _read_env(self):
        """Read the environment from the file `self.filename`."""

        with open(self.filename, "r") as f:
            for line in f:
                temp = []
                for char in line:
                    if char != '\n':
                        temp.append(Node(char))
                self._environment.append(temp)

    def reset(self):
        """Reset the playing field by re-reading the environment
        from the file `self.filename`.
        """

        # this is effectively an alias to _read_env, but a user
        # doesn't necessarily know that, and the two functions
        # may differ in the future.

        self._read_env()

    def __str__(self):
        """Print our env prettily.
        """

        ret = ""
        for line in self.env:
            for node in line:
                ret += str(node)
            ret += '\n'

        return ret

    def search(self, sfunc, start='s', goal='g'):
        """Search through the playing field.

        Params:
        -------
        sfunc : function
            The search function to use.
        start : str
            The (length 1) string to start the search at.
        goal : str
            The (length 1) string to end the search at.
        """

        raise NotImplementedError("Searching not supported yet!")

    @property
    def environment(self):
        """Environment property.
        """

        return self._environment

    @property
    def env(self):
        """Shorthand for environment property.
        """

        return self._environment

    @property
    def filename(self):
        """Filename property.
        """

        return self._filename

    def isBlocked(self,xy):#TODO:
        return False
    def isStart(self,xy):#TODO:
        return False
    def isTarget(self,xy):#TODO:
        return False

if __name__ == '__main__':
    field = PlayingField("blatt3_environment.txt")
    print(field)
