from parameterized import parameterized
from staircase.solution import solution


@parameterized.expand([
    (3, 1),
    (4, 1),
    (5, 2),
    # (200, 487067745)
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

