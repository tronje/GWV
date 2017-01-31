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

    def __str__(self):
        return str(self.variables)


class UnaryConstraint(object):
    """A constraint that describes a condition for just one variable.
    """

    def __init__(self, variable, cfunc):
        self.variable = variable
        self.cfunc = cfunc

    def is_satisfied(self, value):
        return self.cfunc(value)
