"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

from itertools import takewhile

from euler import fib


def main():
    """
    >>> main()
    4613732
    """
    limit = 4000000

    print sum((x for x in takewhile(lambda x: x < limit, fib()) if x % 2 == 0))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
