# -*- coding: utf-8 -*-

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

RESET = '\033[0m'

class Path(object):
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
        self._nodes = [startnode]

        # add all parents to build the path
        # insert at 0 ('prepend') to get the correct order
        while self._nodes[0].parent != None:
            self._nodes.insert(0, self._nodes[0].parent)

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node.coords)
        return ret

    def __len__(self):
        return len(self._nodes)

    def __getitem__(self, key):
        if type(key) is not int:
            return None
        else:
            return self._nodes[key]

    def __contains__(self, item):
        return item in self._nodes

    def pretty(self, exclude=['s', 'g']):
        """Prettily print the path through the given
        PlayingField.

        Params:
        -------
        exclude : list
            A list of nodes' values to not draw over when
            drawing the path.
        """

        # walk over each node in playing field
        for row in self._pfield.env:
            for node in row:
                # if the node is part of the path but not
                # in the exclude list and not a portal...
                if (node in self and node.value not in exclude
                        and not node.is_portal()):
                    # ...print a green dot
                    print(GREEN + '.' + RESET, end='')
                # print portals yellow
                elif node.is_portal():
                    print(YELLOW + str(node) + RESET, end='')
                # print walls in red
                elif node.value == 'x':
                    print(RED + str(node) + RESET, end='')
                else:
                    # otherwise, print the node
                    print(node, end='')
            # print a newline at the end of each row
            print()

