"""
Solution to: The Grandest Staircase Of Them All
"""
from itertools import combinations, chain


def solution(bricks):
    """The number of different staircases that can be built from exactly n bricks

    Args:
        bricks: int, number of bricks used to build the staircase, [3, 200]

    Returns:

    """

    step_size_options = range(1, bricks)
    num_valid_subsets = 0

    # Get all potential staircase arrangements
    for set_option in powerset(step_size_options):

        # If this is a valid staircase arrangement
        if sum(set_option) == bricks and len(set_option) > 1:

            num_valid_subsets += 1

    return num_valid_subsets


def powerset(iterable):
    """Generate powerset (the set of all subsets)

    Args:
        iterable: iterable to generate subsets from

    Returns:
        powerset generator
    """
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
