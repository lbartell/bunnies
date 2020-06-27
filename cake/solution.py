"""
Solution to: The cake is not a lie!
"""


def solution(s):
    """Compute maximum number of equal slices that the cake can be divided into

    Args:
        s: str, a string describing the sequence of M&Ms. String should...
            be non-empty,
            have less than 200 chars, and
            contain one unique character (case-sensitive) for each M&M color.

    Returns:
        num_slices: int, maximum number of equal parts that can be cut from the cake without leaving any leftovers
    """

    # Default to 1 slice
    num_slices = 1

    # The factors of the number of M&Ms define the set of potential options for number of cake slices
    num_m_and_ms = len(s)
    possible_num_slices = _factors(num_m_and_ms)

    # Check each option for number of slices, starting with the largest
    for num_slices in sorted(possible_num_slices, reverse=True):
        slice_size = num_m_and_ms // num_slices
        slices = set(_chunks(s, slice_size))

        # If there is only one unique slice in the set of slices, then we found a valid result
        if len(slices) == 1:
            break

    return num_slices


def _chunks(list_to_chunk, chunk_size):
    """Generator yielding chunks of the given size from the given list

    Args:
        list_to_chunk: list (or similar) of objects to yield in chunks
        chunk_size: length of chunk to return

    Yields:
        chunk: iterable of length chunk_size from the original list
    """
    for index in range(0, len(list_to_chunk), chunk_size):
        yield list_to_chunk[index: index + chunk_size]


def _factors(num):
    """Get a list of factors of the given number

    Args:
        num: integer number

    Returns:
        list of factors, integers that divide evenly into the number
    """
    if num < 1:
        raise ValueError("Factor computation is only valid for non-zero positive integers")
    return [val for val in range(1, num + 1) if num % val == 0]
