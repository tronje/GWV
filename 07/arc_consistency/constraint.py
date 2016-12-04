class Constraint(object):
    def __init__(self, nodes, cfunc):
        self.nodes = nodes
        self.cfunc = cfunc

    def is_satisfied(self, values):
        assert type(values) is list
        return self.cfunc(*values)

    def other_node(self, node):
        for other in self.nodes:
            if other != node:
                return other
