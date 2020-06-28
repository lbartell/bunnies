"""
Solution to: Fuel Injection Perfection
"""


def solution(pellets):
    """Find the minimum number of operations needed to transform the number of pellets to 1

    Args:
        pellets: number of input fuel pellets

    Returns:
        int, minimum number of operations
    """
    return min_operations(0, pellets)


def min_operations(steps, num):
    """Find minimum number of steps required to reduce the given number of pellets

    Args:
        steps: number of steps (operations) performed previously
        num: number of pellets

    Returns:
        int, minimum number of operations required
    """

    # Increment number of steps
    steps += 1

    if num <= 2:
        # If number is 1 or 2, then path is complete
        return steps

    else:
        # Find the number of times 2 appears as a factor
        minus_factors = sum(factor == 2 for factor in factors(num - 1))
        plus_factors = sum(factor == 2 for factor in factors(num + 1))
        if num % 2 == 0:
            divide_factors = sum(factor == 2 for factor in factors(num // 2))
        else:
            divide_factors = - 1

        # Follow the path that is the most divisible by two
        max_factors = max(minus_factors, plus_factors, divide_factors)
        if minus_factors == max_factors:
            # Removing one is best path
            return min_operations(steps, num - 1)

        elif divide_factors == max_factors:
            # Cutting in half is best path
            return min_operations(steps, num // 2)

        else:
            # Adding one is best path
            return min_operations(steps, num + 1)


def factors(num):
    """Return list of factors of the given integer

    Args:
        num: integer, number to factorize

    Returns:
        integer factors of the given number
    """
    factors = []
    while num > 1:
        for index in range(2, num + 1):
            if num % index == 0:
                num /= index
                factors.append(index)
                break
    return factors