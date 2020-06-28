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
    return min_operations(0, int(pellets))


def min_operations(steps, num):
    """Find minimum number of operations required to reduce the given number of pellets

    Args:
        steps: number of operations performed previously
        num: number of pellets

    Returns:
        int, minimum number of operations required
    """
    if num <= 1:
        # If number is 1, then path is complete
        return steps

    else:
        # Otherwise, follow operation that yields the most factors of two
        steps += 1

        plus_one_factors = times_divisible_by_two(num + 1)
        minus_one_factors = times_divisible_by_two(num - 1)
        if num % 2 == 0:
            div_two_factors = times_divisible_by_two(num // 2)
        else:
            div_two_factors = -1

        max_factors = max(plus_one_factors, minus_one_factors, div_two_factors)

        if div_two_factors == max_factors:
            return min_operations(steps, num // 2)

        if minus_one_factors == max_factors:
            return min_operations(steps, num - 1)

        if plus_one_factors == max_factors:
            return min_operations(steps, num + 1)


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