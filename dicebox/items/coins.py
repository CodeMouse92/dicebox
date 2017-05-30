"""
Coin [dicebox 1.0]

Flip any number of coins.

Author(s): Jason C. McDonald
"""

import random

class CoinJar:
    """
    A collection of one or more coins, which can be flipped.
    """

    def __init__(self, count=1):
        """
        Initialize a jar of coins.
        """
        # The list of coins, all Heads by default.
        self.__coins = [True] * count

    def flip(self):
        """
        Flip all coins in the CoinJar.
        True = Heads, False = Tails
        """
        for i in range(0, len(self.__coins)):
            self.__coins[i] = random.choice([True, False])

    def display(self):
        """
        Show the results of the coin flip.
        """
        for coin in self.__coins:
            if coin:
                print("Heads")
            else:
                print("Tails")
