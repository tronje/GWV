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

        # remember the playing field this path lives in
        self._pfield = pfield

        # initialize the path as a list of nodes
        # (containing only the startnode at first)
        nodes = [startnode]

        # add all parents to build the path
        # insert at 0 ('prepend') to get the correct order
        while nodes[0].parent != None:
            nodes.insert(0, nodes[0].parent)

        # assign to self
        self._nodes = nodes

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node.coords)
        return ret

    def __len__(self):
        return len(self._nodes)

    def pretty(self, exclude=['s', 'g']):
        """Prettily print the path through the given
        PlayingField.

        Params:
        -------
        exclude : list
            A list of nodes' values to not draw over when
            drawing the path.
        """

        # save original environment to revert changes later
        env = self._pfield.env.copy()

        for node in self._nodes:
            if node.value in exclude or node.value.isdigit():
                continue
            self._pfield.env[node.x][node.y] = '.'

        print(self._pfield)

        # reset env
        self._pfield.env = env

