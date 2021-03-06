from parameterized import parameterized

from elevator.solution import solution


@parameterized.expand([
    (["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
     ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]),
    (["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
     ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]),
    (["0.0"], ["0.0"]),
    (["1", "0.1", "0.1"], ["0.1", "0.1", "1"]),
    (["1.0.0", "1", "1.0"], ["1", "1.0", "1.0.0"])

])
def test_solution(versions, expected):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(versions)

    # Assert
    assert result == expected
