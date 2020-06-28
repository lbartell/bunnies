"""
Solution to: The Grandest Staircase Of Them All

Simplifies to the Partition Function Q, which gives the number of ways of writing an integer
as a sum of distinct positive integers, disregarding order
"""
from math import sqrt


def solution(n):
    """The number of different staircases that can be built from exactly n bricks

    Args:
        bricks: int, number of bricks used to build the staircase, [3, 200]

    Returns:
        int, number of staircase options
    """

    # Calculate the number of paritions of distinct positive integers
    j_sequence = calc_j_seq(n+1)
    paritions = partition_q(n, j_sequence)

    # Reduce by 1 because we need at least one step
    staircases = paritions - 1

    return staircases


def partition_q(n, j_sequence):
    """Number of ways of writing an integer as a sum of distinct positive integers, disregarding order

    Algorithm implementation based on:
    https://mathworld.wolfram.com/PartitionFunctionQ.html

    Args:
        n: integer number to partition

    Returns:
        number of ways of writing an integer
        as a sum of distinct positive integers, disregarding order
    """
    # Break out if zero
    if n == 0:
        return 1

    sqrt_n = int(sqrt(n)) + 1
    q_sum = sum(
        ((-1) ** (k + 1)) * partition_q(n - k ** 2, j_sequence)
        for k in range(1, sqrt_n)
    )

    return s(n, j_sequence) + 2 * q_sum


def s(n, j_sequence):
    if n in j_sequence:
        return (-1) ** j_sequence[n]

    else:
        return 0


def calc_j_seq(max_n):
    """Used to determine if n of form j*(3*j (+/-) 1) / 2 by creating a dictionary of n, j value pairs

    Args:
        max_n: int, maximum integer to prepare the dictionary for

    Returns:
        dictionary if n, j value pairs
    """
    result = {}
    j = 0
    valn = -1
    while valn <= max_n:
      jj = 3 * j ** 2
      valp, valn = (jj - j) // 2, (jj + j) // 2
      result[valp] = j
      result[valn] = j
      j += 1

    return result


# ========== brute force solutions
from itertools import combinations, chain


def bruce_force_solution(bricks):
    """The number of different staircases that can be built from exactly n bricks

    Args:
        bricks: int, number of bricks used to build the staircase, [3, 200]

    Returns:
        int, number of staircase options
    """
    step_size_options = range(1, bricks)
    num_options = 0
    for option in powerset(step_size_options):
        if len(option) > 1 and sum(option) == bricks:
            num_options += 1

    return num_options


def powerset(iterable):
    """Generate powerset (the set of all subsets)

    Args:
        iterable: iterable to generate subsets from

    Returns:
        powerset generator
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
