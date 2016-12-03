# -*- coding: utf-8 -*-

class Arc(object):
    def __init__(self, constraint, nodes):
        self._constraint = constraint
        self._nodes = nodes

    def is_consistent(self):

