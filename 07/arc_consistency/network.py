from arc_consistency import Arc

class Network(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self._arcs = None
        self.constraints = set()

    @property
    def arcs(self):
        if self._arcs is None:
            self._make_arcs()
        return self._arcs

    def __str__(self):
        ret = ""
        for node in self.nodes:
            ret += str(node)
            ret += '\n'
        return ret

    def _make_arcs(self):
        self._arcs = set()
        for constraint in self.constraints:
            for node in constraint.nodes:
                new_arc = Arc(node, constraint)
                self.arcs.add(new_arc)
                # register the arc with the node as well,
                # so it knows about its arcs
                node.arcs.add(new_arc)

    def get_node(self, meta_key, meta_value):
        """Find a node based on its meta info"""
        for node in self.nodes:
            if node.meta[meta_key] == meta_value:
                return node

    def add_constraint(self, constraint):
        self.constraints.add(constraint)

        # add the constraint to each node as well,
        # so they know about the constraints they are
        # involved in
        for node in constraint.nodes:
            node.constraints.add(constraint)

    def gac(self):
        """Generalized arc consistency algorithm"""

        # initialize todo arcs as all arcs
        todo_arcs = self.arcs

        # while todo_arcs isn't empty
        while len(todo_arcs) > 0:
            arc = todo_arcs.pop()
            if not arc.is_consistent():
                arc.make_consistent()

                for node in self.nodes:
                    for other_arc in node.arcs:
                        if other_arc.other_node() == arc.node:
                            todo_arcs.add(other_arc)

            print(len(todo_arcs))
