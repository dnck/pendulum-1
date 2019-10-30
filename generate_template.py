# -*- coding: utf-8 -*-
program_structure = '''# -*- coding: utf-8 -*-
"""
Module description:
{}
# Style Guide: https://www.python.org/dev/peps/pep-0257/
"""

import argparse
{} # user added modules


{} # Implementation constants, and Program logic


{} # Classes, methods, functions, and variables


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description=""
    )
    PARSER.add_argument("",
        metavar="", type=str, default="",
        help=""
    )

    args = PARSER.parse_args()

    {} # Set up with user given configuration

    main()
'''
with open("test.py", "a") as fname:
    fname.write(program_structure)
