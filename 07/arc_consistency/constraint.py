class Constraint(object):
    """A constraint describes a condition between two or more variables.
    """

    def __init__(self, variables, cfunc):
        self.variables = variables
        self.cfunc = cfunc

    def is_satisfied(self, values):
        assert type(values) is list
        return self.cfunc(*values)

    def other_variable(self, variable):
        for other in self.variables:
            if other != variable:
                return other
