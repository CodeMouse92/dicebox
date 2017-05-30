"""
Socks [dicebox 1.0]

Pull a sock from a sock drawer.

Author(s): Jason C. McDonald
"""

import random

class CardDeck:
    """
    A collection of socks.
    """

    def __init__(self, count=1):
        """
        Initialize a drawer of socks.
        """

        # The cards in the deck.
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5",
                       "4", "3", "2", "Ace"]

        self.deck = ["Joker", "Joker"]

        for value in self.values:
            for suit in self.suits:
                self.deck += [value + " of " + suit]

        # Store the count.
        self.count = count

        # The list of cards, empty by default.
        self.__cards = []

    def draw(self):
        """
        Draw the requested number of cards.
        """
        self.__cards = random.sample(self.deck, self.count)

    def display(self):
        """
        Show the results of the coin flip.
        """
        for card in self.__cards:
            print(card)
