"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
"""

from problem018 import triangle_sum


def main():
    """
    >>> main()
    7273
    """
    with open("triangle.txt") as f:
        triangle = f.read().splitlines()

    triangle = [[int(n) for n in line.split(' ')] for line in triangle]
    triangle.reverse()

    print(reduce(triangle_sum, triangle)[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()