from parameterized import parameterized
from staircase.solution import solution, bruce_force_solution


@parameterized.expand([
    (3, 1),
    (4, 1),
    (5, 2),
    (200, 487067745)
])
def test_solution(n, expected):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(n)

    # Assert
    assert result == expected


@parameterized.expand([(num,) for num in range(15)])
def test_solution_brute(n):
    """
    Test solution
    """
    # Arrange
    expected = bruce_force_solution(n)

    # Act
    result = solution(n)

    # Assert
    assert result == expected
