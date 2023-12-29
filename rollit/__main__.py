"""
Rollit: Dice-based passphrase generator.
"""

import argparse

import pass_generator
from messages import HLP_NUM_WORDS, HLP_SEPARATOR, MSG_PROG_DESCRIPTION


def main():
    """Set up the parser object, arguments, and call `generate_pass`"""

    # Parser object.
    parser = argparse.ArgumentParser(description=MSG_PROG_DESCRIPTION)

    # Arguments.
    parser.add_argument("-n", "--number", default=4, type=int, help=HLP_NUM_WORDS)
    parser.add_argument("-s", "--separator", default="-", type=str, help=HLP_SEPARATOR)

    # Read arguments.
    args = parser.parse_args()

    # Generate passphrase.
    passphrase: str = pass_generator.generate_passphrase(args.number, args.separator)

    # Output.
    print(passphrase)


if __name__ == "__main__":
    main()
