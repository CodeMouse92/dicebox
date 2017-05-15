"""
dicebox 1.0
Main module.

Author(s): Jason C. McDonald
"""

# Process command line arguments.
import sys
from dicebox.items import coins

def coin(args):
    """
    Calls the coin function.
    """

    flips = 1
    # Make sure we have only one argument, an integer.
    if len(args) == 1:
        try:
            flips = int(args[0])
        except ValueError:
            print("Invalid number of coins (" + str(args[0]) + ") provided.")
            sys.exit(1)

    coinjar = coins.CoinJar(flips)
    coinjar.flip()
    coinjar.display()

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
        coin(args)

if __name__ == "__main__":
    main()
