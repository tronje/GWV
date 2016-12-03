class Network(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self._arcs = None

    @property
    def arcs(self):
        if self._arcs is None:
            self._arcs = self._make_arcs()
        return self._arcs

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node)
            ret += '\n'
        return ret

    def _make_arcs(self):
        arcs = []
        for constraint in self.constraints:
            for node in constraint.nodes:
                arcs.append(Arc(node, constraint))
        return arcs

    def gac(self):
        """Generalized arc consistency algorithm"""

        # initialize todo arcs as all arcs
        todo_arcs = self.arcs

        # while todo_arcs isn't empty
        while len(todo_arcs) > 0:
            pass
