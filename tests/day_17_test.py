from main.day_17 import solve_1, solve_2

input = "target area: x=20..30, y=-10..-5"


def test_solve_1():
    assert solve_1(input) == 45


def test_solve_2():
    assert solve_2(input) == 112
