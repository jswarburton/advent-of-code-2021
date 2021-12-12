from main.day_12 import solve_1, solve_2

input = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]


def test_solve_1():
    assert solve_1(input) == 10


def test_solve_2():
    assert solve_2(input) == 36
