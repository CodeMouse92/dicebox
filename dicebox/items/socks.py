"""
Socks [dicebox 1.0]

Pull a sock from a sock drawer.

Author(s): Jason C. McDonald
"""

import random

class SockDrawer:
    """
    A collection of socks.
    """

    def __init__(self, count=1):
        """
        Initialize a drawer of socks.
        """

        # The socks to be found in the drawer.
        self.choices = ["white"] * (4 * count)
        self.choices += ["black"] * (3 * count)
        self.choices += ["red", "blue", "green", "argyle"] * (2 * count)
        self.choices += ["stripey", "fuzzy", "toe"] * (1 * count)

        # Store the count.
        self.count = count

        # The list of socks, empty by default.
        self.__pulls = []

    def rummage(self):
        """
        Roll all dice in the DiceCan.
        """
        self.__pulls = random.sample(self.choices, self.count)

    def display(self):
        """
        Show the results of the coin flip.
        """
        for sock in self.__pulls:
            print(sock)
