from parameterized import parameterized
from baby.solution import solution


@parameterized.expand([
    ("2", "1", "1"),
    ("4", "7", "4"),
    ("2", "4", "impossible"),
])
def test_solution(mach, facula, generations):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(mach, facula)

    # Assert
    assert result == generations

