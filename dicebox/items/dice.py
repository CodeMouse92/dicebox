"""
Dice [dicebox 1.0]

Roll dice of any size and count.

Author(s): Jason C. McDonald
"""

import random

class DiceCan:
    """
    A collection of one or more coins, which can be flipped.
    """

    def __init__(self, count=1, faces=6):
        """
        Initialize a can of dice.
        """
        # The list of dice, all 1 by default.
        self.__dice = [1] * count
        # The number of faces on one die.
        self.__faces = faces

    def roll(self):
        """
        Roll all dice in the DiceCan.
        """
        for i in range(0, len(self.__dice)):
            self.__dice[i] = random.randint(1, self.__faces)

    def display(self):
        """
        Show the results of the coin flip.
        """
        for die in self.__dice:
            print(die)
