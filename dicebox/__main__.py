"""
dicebox 1.0
Main module.

Author(s): Jason C. McDonald
"""

# Process command line arguments.
import sys
from dicebox.items import cards, coins, dice, socks, straws

def use_cards(args):
    """
    Calls the cards function.
    """

    def die():
        """
        Die with an error.
        """
        print("One optional argument:")
        print("  cards (optional): Number of cards to draw, integer "
              + "where n > 0. Default = 1.")
        sys.exit(1)

    # Make sure we have only one argument, an integer.
    if len(args) == 1:
        try:
            draws = int(args[0])
        except ValueError:
            die()
        if draws < 1 or draws > 52:
            die()
    # If we have no arguments, draw one card.
    elif len(args) == 0:
        draws = 1
    # Otherwise, throw an error.
    else:
        die()

    carddeck = cards.CardDeck(draws)
    carddeck.draw()
    carddeck.display()

def use_coins(args):
    """
    Calls the coin function.
    """

    def die():
        """
        Die with an error.
        """
        print("One optional argument:")
        print("  coins (optional): Number of coins, integer where n > 0. " +
              "Default = 1.")
        sys.exit(1)

    # Make sure we have only one argument, an integer.
    if len(args) == 1:
        try:
            flips = int(args[0])
        except ValueError:
            die()
    # If we have no arguments, flip one coin.
    elif len(args) == 0:
        flips = 1
    # Otherwise, throw an error.
    else:
        die()

    coinjar = coins.CoinJar(flips)
    coinjar.flip()
    coinjar.display()

def use_dice(args):
    """
    Calls the dice function.
    """

    def die():
        """
        Die with an error.
        """
        print("One optional argument:")
        print("  roll (optional): String formatted as 'NdF', where N is the "
              + "number of dice, and F is the number of faces on each die. "
              + "N must > 0, F >= 4. Default = 1d6.")
        print("  i.e. 3d6 = roll 3 six-faced dice.")
        sys.exit(1)

    # Make sure we have only one argument, a string.
    if len(args) == 1:
        # Split string by the 'd'.
        split = str(args[0]).partition("d")
        try:
            rolls = int(split[0])
            faces = int(split[2])
        except ValueError:
            die()
    # If we have no arguments, use 1d6
    elif len(args) == 0:
        rolls = 1
        faces = 6
    # Otherwise, throw an error.
    else:
        die()

    # Make sure our numbers are valid.
    if rolls < 1 or faces < 4:
        die()

    dicecan = dice.DiceCan(rolls, faces)
    dicecan.roll()
    dicecan.display()

def use_socks(args):
    """
    Calls the sock function.
    """

    def die():
        """
        Die with an error.
        """
        print("One optional argument:")
        print("  count (optional): number of socks, integer where n > 0. "
              + "Default = 1")
        sys.exit(1)

    # Make sure we have only one argument, an integer.
    if len(args) == 1:
        try:
            pulls = int(args[0])
        except ValueError:
            die()
    # If we have no arguments, draw one sock.
    elif len(args) == 0:
        pulls = 1
    # Otherwise, throw an error.
    else:
        die()

    sockdrawer = socks.SockDrawer(pulls)
    sockdrawer.rummage()
    sockdrawer.display()

def use_straws(args):
    """
    Calls the straws function.
    """

    def die():
        """
        Die with an error.
        """
        print("One argument required, three optional, all integers:")
        print("  count (required): the number of straws, integer where n > 0.")
        print("  short (optional): the number of short straws, integer " +
              "where 0 < n > count. Default = 1")
        print("  draws (optional): the number of straws to draw, integer " +
              "where n > 0. Default = count")
        sys.exit(1)

    # Make sure we have 1-3 arguments, all integers.
    try:
        if len(args) == 1:
            count = int(args[0])
            short = 1
            draws = 0
        elif len(args) == 2:
            count = int(args[0])
            short = int(args[1])
            draws = 0
        elif len(args) == 3:
            count = int(args[0])
            short = int(args[1])
            draws = int(args[2])
        # Otherwise, throw an error.
        else:
            die()
    except ValueError:
        die()

    if count < 1 or short < 1 or short > count or (len(args) == 3 and draws < 1):
        die()

    strawbundle = straws.StrawBundle(count, short, draws)
    strawbundle.draw()
    strawbundle.display()

def main():
    """
    The main function for dicebox.
    """
    args = []
    if len(sys.argv) <= 1:
        print("Specify a mode and its arguments.")
        print("Arguments: <required>, [optional=default]")
        print("  cards [N=1]: Draw [N] playing cards.")
        print("  coin [N=1]: Flip [N] coins.")
        print("  dice [N=1]d[F=6]: Roll [N] dice with [F] faces.")
        print("  sock [N=1]: Draw [N] socks from a drawer.")
        print("  straws <N> [S=1], [D=N]: Draw [D] straws, from a bundle of " +
              "<N> straws with [S] short straws.")
        sys.exit(1)
    elif len(sys.argv) >= 2:
        args = sys.argv[2:]

    item = sys.argv[1]
    if item == "card" or item == "cards":
        use_cards(args)
    elif item == "coin":
        use_coins(args)
    elif item == "die" or item == "dice":
        use_dice(args)
    elif item == "sock" or item == "socks":
        use_socks(args)
    elif item == "straw" or item == "straws":
        use_straws(args)

if __name__ == "__main__":
    main()
