from parameterized import parameterized
from salute.solution import solution


@parameterized.expand([
    ("--->-><-><-->-", 10),
    (">----<", 2),
    ("<<>><", 4),
    ("<<>><", 4),
    ("----", 0),
    ("<", 0),
    (">", 0),
    ("-", 0),
    ("<>>>>>", 0),
    ("<<<<<<>>", 0),
    (">>>>", 0),
])
def test_solution(hallway, salutes):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(hallway)

    # Assert
    assert result == salutes

