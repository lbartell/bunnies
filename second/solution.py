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
    # Convert strings to semantic version objects
    semantic_versions = [SemanticVersion.from_string(semver_string) for semver_string in l]

    # Sort by major, minor, revision
    sorted_versions = sorted(semantic_versions, key=lambda ver: ver.as_tuple())

    # Convert to string representation
    sorted_version_strings = [str(ver) for ver in sorted_versions]

    return sorted_version_strings


class SemanticVersion:
    """
    Class to hold semantic version information
    """

    def __init__(self, major=0, minor=-1, revision=-1):
        """Initialize

        Args:
            major: int, major version, defaults to zero
            minor: int, minor version
            revision: int revision version

        Notes:
            minor and revision numbers default to -1, representing _no_ version number specified
        """
        self.major = major
        self.minor = minor
        self.revision = revision

    def __str__(self):
        """Display version as a string

        Returns:
            str display of semantic version
        """
        if self.revision >= 0:
            string = f"{self.major}.{self.minor}.{self.revision}"

        elif self.minor >= 0:
            string = f"{self.major}.{self.minor}"

        else:
            string = f"{self.major}"

        return string

    @classmethod
    def from_string(cls, symver_string):
        """Create semantic version from given string representation
        Args:
            symver_string: string representing the semantic version, e.g. "1" or "1.0", or "0.2.6"

        Returns:
            Instance of SemanticVersion corresponding to the given string
        """
        # Initialize default version major, minor, and revision numbers
        version_list = []

        # Split string by periods to extract each version number
        for num_string in symver_string.split("."):
            if num_string:  # If string is not empty
                version_list.append(int(num_string))

        # Create new class instance based on the extracted numbers
        return cls(*version_list)

    def as_tuple(self):
        """Return tuple representation of the version"""
        return (self.major, self.minor, self.revision)
