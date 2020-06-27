"""
Solution to: Elevator Maintenance
"""


def solution(l):
    """Sort given elevator versions by major, minor, revision

    Args:
        l: (unordered) list of elevator versions represented as strings

    Returns:
        ordered_versions: ordered list of elevators versions, by increasing semantic version
    """
    return sorted(l, key=lambda ver: tuple(int(num) for num in ver.split(".")))
