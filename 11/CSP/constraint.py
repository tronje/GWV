class Constraint(object):
    def __init__(self, s, summands):
        self.sum = s
        self.summands = summands

    def satisfied():
        # missing consideration of overflows!
        # e.g. 9 + 2 = 1, in single-digit integer addition!
        return sum(self.summands) == self.sum
