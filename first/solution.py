import string


def solution(s):
    """The cake is not a lie! Compute maximum number of equal slices

    Args:
        s: str, a non-empty string less than 200 characters in length describing the sequence of M&Ms (letters a-z)

    Returns:
        num_slices: int, maximum number of equal parts that can be cut from the cake without leaving any leftovers
    """
    # Clean and validate input
    s = _validate_input(s)

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


def _validate_input(s):
    """Assert input is valid and return cleaned string

    Check input...
    - is a string
    - has expected length [1, 200]
    - only includes letter characters

    Clean up string
    - convert to all lowercase
    - remove any white space chars

    Args:
        s: string input

    Raises:
        AssertionError if any of the checks are not met

    Returns:
        s: string, validated and cleaned
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string input. Instead found type {type(s)}.")
    if len(s) < 0 or len(s) > 200:
        raise ValueError(f"Expected string of length [1, 200]. Instead found length {len(s)}.")

    # Clean up string: lowercase and remove whitespace
    s_lower = s.lower()
    s_cleaned = "".join(s_lower.split())

    if len(set(s_cleaned) - set(string.ascii_lowercase)) > 0:
        raise ValueError(f"Expected string to contain only ASCII letters. Instead got {s}.")

    return s_cleaned


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
