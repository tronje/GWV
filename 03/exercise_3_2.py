#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlayingField(object):
    """Represents a playing field, which is read
    from a file and stored in a 2d-list.
    Can be printed and (TODO) searched through.
    """

    def __init__(self, filename):
        """Initialize a playing field.

        Params:
        -------
        filename : str
            The name of the file from which to read
            the playing field.
        """

        # name of the file to use
        self._filename = filename

        # our virtual environment
        self._environment = []

        # read env from the file
        with open(filename, "r") as f:
            for line in f:
                self._environment.append(list(line))

        # remove newlines, they're not relevant to us
        for elem in self._environment:
            elem.remove('\n')

    def __str__(self):
        """Print our env prettily.
        """

        ret = ""
        for line in self.env:
            for char in line:
                ret += char
            ret += '\n'

        return ret

    def search(self, sfunc, start='s', goal='g'):
        """Search through the playing field.

        Params:
        -------
        sfunc : function
            The search function to use.
        start : str
            The (length 1) string to start the search at.
        goal : str
            The (length 1) string to end the search at.
        """

        raise NotImplementedError("Searching not supported yet!")

    @property
    def environment(self):
        """Environment property.
        """

        return self._environment

    @property
    def env(self):
        """Shorthand for environment property.
        """

        return self._environment

def main():
    # create playing field object from the txt file
    field = PlayingField("blatt3_environment.txt")
    # print, to see if it worked
    print(field)

    # try the other file as well
    field = PlayingField("blatt3_environment_b.txt")
    print(field)

if __name__ == '__main__':
    main()
