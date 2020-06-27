from pytest import mark, raises

from cake.solution import solution, _factors, _chunks


@mark.parametrize("num, factors", [
    (1, [1]),
    (2, [1, 2]),
    (10, [1, 2, 5, 10])
])
def test_factors(num: int, factors: list) -> None:
    """
    Test factors
    """
    # Arrange

    # Act
    result = _factors(num)

    # Assert
    assert result == factors


@mark.parametrize("num", [-100, 0])
def test_factors_error(num) -> None:
    """
    Test factors raises error with invalid input
    """
    # Arrange
    num = 0

    # Act / assert
    with raises(ValueError):
        _factors(num)


@mark.parametrize("s, num_slices", [
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
def test_solution(s: str, num_slices: int) -> None:
    """
    Test cake cutting solution
    """
    # Arrange

    # Act
    result = solution(s)

    # Assert
    assert result == num_slices
