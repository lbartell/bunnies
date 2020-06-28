"""
Solution to: Bomb, Baby!
"""


def solution(mach, facula):
    """Find fewest generations needed to generate the given number of bombs of each type

    Args:
        mach: str, integer number of Mach bombs, [1, 10^50]
        facula: str, integer number of Facula bombs, [1, 10^50]

    Returns:
        str, fewest number of generations needed, or "impossible"
    """
    m = int(mach)
    f = int(facula)
    generations = 0

    while not (m == f == 1):
        if f == 1:
            # If only one F bomb, subtract as many times as needed
            generations += m - 1
            m = 1

        elif m == 1:
            # If only one M bomb, subtract as many times as needed
            generations += f - 1
            f = 1

        elif m > f > 1:
            # Subtract number of F bombs from the M bomb count, as many times as possible
            generations += m // f
            m = m % f

        elif f > m > 1:
            # Subtracted number of M bombs from the F bomb count, as many times as possible
            generations += f // m
            f = f % m

        else:  # if m == f or m < 1 or f < 1
            return "impossible"

    return str(generations)
