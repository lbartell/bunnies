from parameterized import parameterized

from cake.solution import solution, _factors


@parameterized.expand([
    (1, [1]),
    (2, [1, 2]),
    (10, [1, 2, 5, 10])
])
def test_factors(num, factors):
    """
    Test factors
    """
    # Arrange

    # Act
    result = _factors(num)

    # Assert
    assert result == factors


@parameterized.expand([
    ("abcabcabcabc", 4),
    ("abccbaabccba", 2),
    ("abcabcabcabc", 4),
    ("abccbaabccba", 2),
    ("abcdefghijklmnopqrstuvwxyz", 1),
    ("a", 1),
    ("abcdefedcba", 1),
    ("aaaaaaa", 7),
    ("zxcvbnm", 1),
])
def test_solution(s, num_slices):
    """
    Test cake cutting solution
    """
    # Arrange

    # Act
    result = solution(s)

    # Assert
    assert result == num_slices
