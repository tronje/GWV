class Arc(object):
    """An arc points from a variable to a constraint
    """

    def __init__(self, variable, constraint):
        self.variable = variable
        self.constraint = constraint

    def other_variable(self):
        return self.constraint.other_variable(self.variable)

    def is_consistent(self):
        other_variable = self.other_variable()

        for elem in self.variable.domain:
            for other in other_variable.domain:
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
        other_variable = self.other_variable()

        # find non-consistent elements
        for elem in self.variable.domain:
            for other in other_variable.domain:
                if self.constraint.is_satisfied([elem, other]):
                    break
            else:
                # for's else is executed if the loop
                # was *not* interrupted by a break!
                non_consistent.append(elem)

        # remove non-consistent elements from domain
        for elem in non_consistent:
            self.variable.domain.remove(elem)
