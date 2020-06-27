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
    return sorted(l, key=semantic_version_tuple)


def semantic_version_tuple(version_string):
    """Convert semantic version string to tuple representation

    Args:
        version_string: str, version string, e.g. "1", "0.1", "1.2.3"

    Returns:
        tuple of major, minor, revision integers
    """
    return tuple(int(num) for num in version_string.split("."))
