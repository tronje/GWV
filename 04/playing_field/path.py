# -*- coding: utf-8 -*-

class Path(list):
    """Collects a Path of nodes starting with a node
    iterating through parents, until a node without
    a parent is found, which is assumed to be the start.
    """

    def __init__(self, startnode, pfield):
        """Initialize a Path starting from a given
        node.

        Params:
        -------
        startnode : Node
            The node to start the path from.
        pfield : PlayingField
            The PlayingField in which the Path lives.
        """

        # remember the playing field we are being used for
        self._pfield = pfield

        # initialize the path as a list of nodes
        # (containing only the startnode at first)
        nodes = [startnode]

        # add all parents to build the path
        while nodes[-1].parent != None:
            nodes.append(nodes[-1].parent)

        # reverse to get the correct order
        nodes.reverse()

        # assign to a field of self
        self.nodes = nodes

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node.coords)
        return ret

    def pretty(self):
        """Prettily print the path through the given
        PlayingField.
        """

        # save original environment to revert changes later
        env = self._pfield.env.copy()

        for node in self.nodes:
            if node.value in ['s', 'g'] or node.value.isdigit():
                continue
            self._pfield.env[node.x][node.y] = '.'

        print(self._pfield)

        # reset env
        self._pfield.env = env

