#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys


def area_of_rectangle(height, width=None):
    """
    Returns the area of a rectangle.
    """
    if width is None:
        width = height
    return height * width


if __name__ == '__main__':
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        message = (
            f"{sys.argv[0]}: Expecting one or two command-line arguments:\n"
            "\tthe height of a square or the height and width of a rectangle"
        )
        sys.exit(message)

    height = float(sys.argv[1])

    if len(sys.argv) == 3:
        width = float(sys.argv[2])
    else:
        width = height

    area = area_of_rectangle(height, width)

    print(f"The area of a {height} X {width} rectangle is {area}")
