"""
dicebox 1.0
Main module.

Author(s): Jason C. McDonald
"""

# Process command line arguments.
import sys
from dicebox.items import coins, dice, socks

def use_coins(args):
    """
    Calls the coin function.
    """

    flips = 1

    def die():
        """
        Die with an error.
        """
        print("Argument must be an integer specifying number of coins, > 0.")
        print("If no argument is specified, a single coin is flipped.")
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

    rolls = 1
    faces = 6

    def die():
        """
        Die with an error.
        """
        print("Argument must be formatted as NdF, where N is the number of \
dice, and F is the number of faces on each die. N and F must be >= 0.")
        print("i.e. 3d6 = roll 3 six-faced dice.")
        print("If no argument is specified, 1d6 is used.")
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

    # Make sure our numbers are > 0
    if rolls <= 0 or faces <= 0:
        die()

    dicecan = dice.DiceCan(rolls, faces)
    dicecan.roll()
    dicecan.display()

def use_socks(args):
    """
    Calls the sock function.
    """

    pulls = 1

    def die():
        """
        Die with an error.
        """
        print("Argument must be an integer specifying number of socks, > 0.")
        print("If no argument is specified, a single sock is drawn.")
        sys.exit(1)

    # Make sure we have only one argument, an integer.
    if len(args) == 1:
        try:
            pulls = int(args[0])
        except ValueError:
            die()
    # If we have no arguments, flip one coin.
    elif len(args) == 0:
        pulls = 1
    # Otherwise, throw an error.
    else:
        die()

    sockdrawer = socks.SockDrawer(pulls)
    sockdrawer.rummage()
    sockdrawer.display()

def main():
    """
    The main function for dicebox.
    """
    args = []
    if len(sys.argv) <= 1:
        print("Argument required.")
        sys.exit(1)
    elif len(sys.argv) >= 2:
        args = sys.argv[2:]

    item = sys.argv[1]
    if item == "coin":
        use_coins(args)
    elif item == "die" or item == "dice":
        use_dice(args)
    elif item == "sock" or item == "socks":
        use_socks(args)

if __name__ == "__main__":
    main()
