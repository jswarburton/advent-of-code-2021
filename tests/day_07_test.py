from main.day_07 import solve_1, solve_2

input = ["16,1,2,0,4,2,7,1,2,14"]


def test_solve_1():
    assert solve_1(input) == 37


def test_solve_2():
    assert solve_2(input) == 168
