class Variable(object):
    """A variable, or variable, within a CSP network.
    """

    def __init__(self, domain=None, meta={}):
        if domain is None:
            self.domain = set()
        else:
            self.domain = domain
        self.meta = meta
        self.arcs = set()

    def __str__(self):
        return str("Variable {") + '\n' \
             + '\t' + str(self.meta) + '\n' \
             + '\t' + str(self.domain) + '\n' \
             + '}'
