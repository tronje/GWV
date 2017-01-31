from csp import Arc

class Network(object):
    """A CSP-network, consisting of variables, arcs and constraints.
    """

    def __init__(self, variables):
        self.variables = variables
        self._arcs = None
        self.constraints = []
        self.unary_constraints = []

    @property
    def arcs(self):
        if self._arcs is None:
            self._make_arcs()
        return self._arcs

    def __str__(self):
        ret = ""
        for variable in self.variables:
            ret += str(variable)
            ret += '\n'
        return ret

    def _make_arcs(self):
        self._arcs = set()
        for constraint in self.constraints:
            for variable in constraint.variables:
                new_arc = Arc(variable, constraint)
                self.arcs.add(new_arc)
                # register the arc with the variable as well,
                # so it knows about its arcs
                variable.arcs.add(new_arc)

    def get_variable(self, meta_key, meta_value):
        """Find a variable based on its meta info"""
        for variable in self.variables:
            try:
                if variable.meta[meta_key] == meta_value:
                    return variable
                elif type(variable.meta[meta_key]) is list:
                    if meta_value in variable.meta[meta_key]:
                        return variable
            except KeyError:
                continue

    def is_solved(self):
        for variable in self.variables:
            if len(variable.domain) != 1:
                return False
        return True

    def satisfy_unary_constraints(self):
        """For each unary constraint, adjust its variable's domain
        so that the constraint is satisfied.
        """

        # simply remove all elements of a variable's domain
        # that contradict the unary constraint
        for uc in self.unary_constraints:
            non_consistent = []
            for elem in uc.variable.domain:
                if not uc.is_satisfied(elem):
                    non_consistent.append(elem)
            for elem in non_consistent:
                uc.variable.domain.remove(elem)

    def gac(self):
        """Generalized arc consistency algorithm"""

        # initialize todo arcs as all arcs
        todo_arcs = self.arcs

        # take care of unary constraints
        self.satisfy_unary_constraints()

        # while todo_arcs isn't empty
        while len(todo_arcs) > 0:
            # grab an arc
            arc = todo_arcs.pop()

            # if it's not consistent...
            if not arc.is_consistent():
                # ... make it consistent
                arc.make_consistent()

                # ... and find all arcs that may have become
                # inconsistent as a result.
                # add those to the todo arcs
                for variable in self.variables:
                    for narc in variable.arcs:
                        # the variable opposite the arc's variable
                        # needs to be our current variable,
                        # and it needs to be from a different
                        # constraint!
                        if (narc.other_variable() == arc.variable
                           and narc.constraint != arc.constraint):
                            todo_arcs.add(narc)

