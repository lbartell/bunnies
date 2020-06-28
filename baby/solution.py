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

    while True:
        if m == f == 1:
            return str(generations)

        elif m > f:
            # Subtract number of F bombs from the M bomb count
            generations += 1
            m -= f

        elif f > m:
            # Subtracted number of M bombs from the F bomb count
            generations += 1
            f -= m

        else:  # if m == f
            return "impossible"
