from parameterized import parameterized
from fuel.solution import solution


@parameterized.expand([
    # ('4', 2),  # 4 > 2 > 1
    # ('15', 5),  # 15 > 16 > 8 >4 > 2 > 1
    # ('2', 1),  # 2 > 1
    # ('8', 3),  #
    # ("17", 5),  #
    ("20", 5),  # 20, 10, 5, 4, 2, 1
    # ("1", 0),
    # ("2", 1)
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

