# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value, metadata={}):
        self._value = value
        self._meta = metadata

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __eq__(self, other):
        return (type(self) == type(other)
            and self.value == other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __getitem__(self, key):
        return self._meta[key]

