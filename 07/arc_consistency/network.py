from arc_consistency import Arc

class Network(object):
    """A CSP-network, consisting of nodes, arcs and constraints.
    """

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

    def gac(self):
        """Generalized arc consistency algorithm"""

        # initialize todo arcs as all arcs
        todo_arcs = self.arcs

        # while todo_arcs isn't empty
        while len(todo_arcs) > 0:
            # grab an arc
            arc = todo_arcs.pop()

            # if it's not consistent...
            if not arc.consistent:
                # ... make it consistent
                arc.make_consistent()

                # ... and find all arcs that may have become
                # inconsistent as a result.
                # add those to the todo arcs
                for node in self.nodes:
                    for narc in node.arcs:
                        # the node opposite the arc's node
                        # needs to be our current node,
                        # and it needs to be from a different
                        # constraint!
                        if (narc.other_node() == arc.node
                                and narc.constraint != arc.constraint):
                            todo_arcs.add(narc)

            # print(len(todo_arcs))
            # p = True
            # for node in self.nodes:
            #     if len(node.domain) > 4:
            #         p = False
            #         break
            #
            # if p:
            #     for node in self.nodes:
            #         print(node.meta['name'], node.domain)
