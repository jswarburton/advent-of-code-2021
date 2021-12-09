from main.day_09 import solve_1, solve_2

input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def test_solve_1():
    assert solve_1(input) == 15


def test_solve_2():
    assert solve_2(input) == 1134
