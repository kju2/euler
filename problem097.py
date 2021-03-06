"""
The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2^6972593 - 1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433 * 2^7830457 + 1.

Find the last ten digits of this prime number.
"""


def main():
    """
    >>> main()
    8739992577
    """
    prime = 2
    for _ in range(7830456 / 24):
        prime *= 2 ** 24
        prime = int(str(prime)[-10:])

    prime = prime * 28433 + 1
    print(int(str(prime)[-10:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
