# -*- coding: utf-8 -*-

class Constraint(object):
    def __init__(self, cfunc):
        """Initialize a constraint with a
        constraint function.
        """

        self._cfunc = cfunc

    def is_satisfied(self, values):
        assert type(values) is list
        return self._cfunc(*values)
