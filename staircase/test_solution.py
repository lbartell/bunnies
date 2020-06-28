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


@parameterized.expand([
    (3,),
    (4,),
    (5,),
    (6,),
    (7,),
    (8,),
    (9,),
    (10,),
    (11,),
])
def test_solution_brute(n):
    """
    Test solution
    """
    # Arrange
    expected = bruce_force_solution(n)
    print "Expected: " + str(expected)

    # Act
    result = solution(n)
    print "Actual: " + str(result)

    # Assert
    assert result == expected

