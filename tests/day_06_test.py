from main.day_06 import solve_1, solve_2

input = ["3,4,3,1,2"]


def test_solve_1():
    assert solve_1(input) == 5934


def test_solve_2():
    assert solve_2(input) == 26984457539
