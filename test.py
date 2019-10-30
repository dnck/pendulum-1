# -*- coding: utf-8 -*-
"""
Module description:
{}
# Style Guide: https://www.python.org/dev/peps/pep-0257/
"""

import argparse
import os


def main(directory):
    for a, b, c, in os.walk(directory):
        print(a, b, c)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="dir search"
    )
    PARSER.add_argument("d",
        metavar="directory", type=str, default="./",
        help="Path to search"
    )

    args = PARSER.parse_args()

    main(args.d)
