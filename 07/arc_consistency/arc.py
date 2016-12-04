class Arc(object):
    def __init__(self, node, constraint):
        """An arc points from a node to a constraint/
        """

        self.node = node
        self.constraint = constraint

    def other_node(self):
        return self.constraint.other_node(self.node)

    def is_consistent(self):
        other_node = self.constraint.other_node(self.node)
        for elem in self.node.domain:
            for other in other_node.domain:
                if self.constraint.is_satisfied([elem, other]):
                    break
            else:
                # for's else is executed if the loop
                # was *not* interrupted by a break!
                # so, if we didn't find at least one match,
                # it's not consistent
                return False
        return True

    def make_consistent(self):
        non_consistent = []
        other_node = self.constraint.other_node(self.node)

        # find non-consistent elements
        for elem in self.node.domain:
            for other in other_node.domain:
                if self.constraint.is_satisfied([elem, other]):
                    break
            else:
                # for's else is executed if the loop
                # was *not* interrupted by a break!
                non_consistent.append(elem)

        # remove non-consistent elements from domain
        for elem in non_consistent:
            self.node.domain.remove(elem)
