from parameterized import parameterized
from fuel.solution import solution


@parameterized.expand([
    (4, 2),
    (15, 5),
    (2, 1),
    (8, 3),
])
def test_solution(pellets, salutes):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(pellets)

    # Assert
    assert result == salutes

