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
    num_valid_subsets = subsets_matching_total(step_size_options, bricks)

    return num_valid_subsets


def subsets_matching_total(my_list, total_sum):
    """Return number of subset of my_list that add up to total_sum"""
    count = 0

    # If the list is short, see if it sums
    if len(my_list) <= 2:
        if sum(my_list) == total_sum:
            count += 1

    # Otherwise, break down the list
    else:
        # Add number of valid subsets of length 2
        if my_list[0] > 1:
            num_two_subsets = len(my_list[: - my_list[0] + 1]) // 2
        else:
            num_two_subsets = len(my_list) // 2
        count += num_two_subsets
        print str(num_two_subsets) + " tuples totaling " + str(total_sum) + " in " + str(my_list)

        # Add number of valid subsets based on the first element, plus other middle elements
        count += subsets_matching_total(
            my_list=my_list[1: - my_list[0]],
            total_sum=total_sum - my_list[0]
        )

    print "count: " + str(count) + " sum: " + str(total_sum) + " my_list: " + str(my_list)
    return count


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
