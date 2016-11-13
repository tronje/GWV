#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import searching

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

class Path(list):
    """Collects a Path of nodes starting with a node
    iterating through parents, untill a node without
    a Parent.
    """
    def __init__(self, startnode):
        """Initialize a Path starting from a given
        node.
        Builds a list by appending the parent of the
        last item in the list to the list. The List
        is then reversed to reflect the walked path.

        Params:
        -------
        startnode : Node
            The node to start the path from.
        """
        print("building path")
        nodes = [startnode]
        while nodes[-1].parent != None:
            nodes.append(nodes[-1].parent)
        nodes.reverse()
        self.nodes = nodes

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node.coords)
        return ret

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
            for line_index, line in enumerate(f):
                temp = []
                for char_index, char in enumerate(line):
                    if char != '\n':
                        temp.append(Node(char, (line_index, char_index)))
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
        node = sfunc(self.env[:], self.findStartNode())
        path = Path(node)
        print(path)

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
        '''

        :param xy:
        :return: boolean
        '''
        return False
    def isStart(self,xy):#TODO:
        '''

        :param xy: Node
        :return: boolean
        '''
        return xy.value == 's'
    def isTarget(self,xy):#TODO:
        '''

        :param xy:
        :return: boolean
        '''
        return False
    def isPortal(self,xy):#TODO:
        '''

        :param xy:
        :return: None/xy-target
        '''
        return None

    def findStartNode(self):
        """Find the start Node in the PlayingField
        return: Node with value == 's'
        """
        for x in range(len(self.env)):
            for y in range(len(self.env[x])):
                current = self.env[x][y]
                if current.value == 's':
                    return current


if __name__ == '__main__':
    field = PlayingField("blatt3_environment.txt")
    print("Start: " + str(field.findStartNode()))
    print(field)
    field.search(searching.bfs)
