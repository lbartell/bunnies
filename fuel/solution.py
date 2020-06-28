"""
Solution to: Fuel Injection Perfection
"""


def solution(pellets):
    """Find the minimum number of operations needed to transform the number of pellets to 1

    Args:
        pellets: string, specifying number of input fuel pellets

    Returns:
        int, minimum number of operations
    """
    n = int(pellets)
    operations = 0

    while n > 1:
        # We will be performing an operation
        operations += 1

        # Always best to divide by two, if possible
        if n % 2 == 0:
            n = n // 2

        # Catch the edge case of 3, should subtract
        elif n == 3:
            n -= 1

        # Decide between adding and subtracting by which result is more divisible by two
        elif times_divisible_by_two(n - 1) > times_divisible_by_two(n + 1):
            n -= 1

        else:
            n += 1

    return operations


def times_divisible_by_two(num):
    """Determine the number of times the given number is divisible by 2

    Count number of trailing zeros in binary representation

    Args:
        num: integer number

    Returns:
        int, number of times the given number is divisible by 2
    """
    string = bin(num)
    count = 0
    for char in reversed(string):
        if char == "0":
            count += 1
        else:
            break

    return count
