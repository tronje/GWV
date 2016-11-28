# -*- coding: utf-8 -*-

from .node import Node
from .path import Path

class PlayingField(object):
    """Represents a playing field, which is read
    from a file and stored in a 2d-list.
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

    def search(
            self,
            sfunc,
            start='s',
            goal='g',
            wall='x',
            info=False,
            progress=False):
        """Search through the playing field.

        Params:
        -------
        sfunc : function
            The search function to use.
        start : str
            The (length 1) string to start the search at.
        goal : str
            The (length 1) string to end the search at.

        Returns:
        --------
        Path object.
        """

        node = sfunc(
                self,
                self.find_node(start),
                goal=goal,
                wall=wall,
                info=info,
                progress=progress)

        path = Path(node, self)
        return path

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

    @env.setter
    def env(self, value):
        """Env setter"""

        self._environment = value

    @property
    def filename(self):
        """Filename property.
        """

        return self._filename

    def find_node(self, value):
        """Find a Node in the PlayingField with
        given value
        return: Node with node.value == value
        """
        for x in range(len(self.env)):
            for y in range(len(self.env[x])):
                current = self.env[x][y]
                if current.value == value:
                    return current

    def find_start_node(self, svalue='s'):
        """Find the start Node in the PlayingField
        return: Node with value == svalue
        """
        return self.find_node(svalue)

    def find_goal_node(self, gvalue='g'):
        """Find the goal Node in the PlayingField
        return: Node with value == gvalue
        """
        return self.find_node(gvalue)

    def find_portal_exit(self, node):
        """Given a portal node, find the other portal with the same value.
        """

        for x in range(len(self.env)):
            for y in range(len(self.env[x])):
                current = self.env[x][y]
                # values must be equal, but they may not be the same object of course!
                if current.value == node.value and current != node:
                    return current
