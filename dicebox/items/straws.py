"""
Straws [dicebox 1.0]

Draw straws.

Author(s): Jason C. McDonald
"""

import random

class StrawBundle:
    """
    A bundle of straws, one of which is short.
    """

    def __init__(self, count=1, short=1, draws=0):
        """
        Initialize a bundle of straws.
        """
        # The number of straws in the bundle.
        self.__count = count
        # The number of short straws in the bundle.
        self.__short = short
        # The number of straws to draw.
        self.__draws = draws
        # If unspecified, we will draw all the straws.
        if self.__draws == 0:
            self.__draws = self.__count

        # The straws drawn.
        self.__drawn = []

        # Generate the bundle of straws.
        self.__straws = [True] * self.__short
        self.__straws += [False] * (self.__count - self.__short)

    def draw(self):
        """
        Draw straws.
        """
        self.__drawn = random.sample(self.__straws, self.__draws)

    def display(self):
        """
        Show the results of the straw draw.
        """
        for i in range(0, len(self.__drawn)):
            if self.__drawn[i]:
                print(str(i+1) + ". You drew a short straw!")
            else:
                print(str(i+1) + ". You're okay.")
