from parameterized import parameterized
from fuel.solution import solution


@parameterized.expand([
    ("2", "1", 1),
    ("4", "7", 4),
])
def test_solution(mach, facula, salutes):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(mach, facula)

    # Assert
    assert result == salutes

