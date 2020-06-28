from parameterized import parameterized
from staircase.solution import solution


@parameterized.expand([
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

