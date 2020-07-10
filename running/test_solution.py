from parameterized import parameterized
from running.solution import solution


@parameterized.expand([
    ([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1, [1, 2]),
    ([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3, [0, 1]),
    ([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 4, [0, 1, 2]),
    ([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 10, [0, 1, 2]),
    ([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 0, [1]),
])
def test_solution(times, time_limit, expected):
    """
    Test solution
    """
    # Arrange

    # Act
    result = solution(times, time_limit)

    # Assert
    assert result == expected

"""
[
    [0, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 1], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0]
]



[
[0, 2, 2, 2, -1], 
[9, 0, 2, 2, -1], 
[9, 3, 0, 2, -1], 
[9, 3, 2, 0, -1], 
[9, 3, 2, 2,  0]
]


[
[ 0, 2, 2, 2, 1], 
[-5, 0, 2, 2, 1], 
[-1, 3, 0, 2, 1], 
[-1, 3, 2, 0, 1], 
[-1, 3, 2, 2, 0]
]
Start End Delta Time Status
    -   0     -    1
    0   1     2   -1
    


Start End Delta Time Status
    -   0     -    0 Bulkhead initially open
    0   4    -1    1
    4   2     2    -1
    2   4    -1    0
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

"""