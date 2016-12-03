class Node(object):
    def __init__(self, domain=None, value=None, meta={}):
        if domain is None:
            self.domain = set()
        else:
            self.domain = domain
        self.value = value
        self.meta = meta

    def __str__(self):
        return str(self.value) + '\n' \
             + str(self.domain) + '\n' \
             + str(self.meta)

