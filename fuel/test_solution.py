from parameterized import parameterized
from fuel.solution import solution


@parameterized.expand([
    ("1", 0),  # 1
    ("2", 1),  # 2 > 1
    ("3", 2),  # 3 > 2 > 1
    ('4', 2),  # 4 > 2 > 1
    ("5", 3),  # 5 > 4 > 2 > 1
    ("6", 3),  # 6 > 3 > 2 > 1
    ("7", 4),  # 7 > 6 > 3 > 2 > 1
    ('8', 3),  # 8 > 4 > 2 > 1
    ("9", 4),  # 9 > 8 > 4 > 2 > 1
    ("10", 4),  # 10 > 5 > 4 > 2 > 1
    ("11", 5),  # 11 > 10 > 5 > 4 > 2 > 1
    ('15', 5),  # 15 > 16 > 8 > 4 > 2 > 1
    ("17", 5),  # 17 > 16 > 8 > 4 > 2 > 1
    ("20", 5),  # 20 > 10 > 5 > 4 > 2 > 1
    ("768", 10),  #
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

