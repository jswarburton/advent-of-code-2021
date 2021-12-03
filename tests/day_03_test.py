from main.day_03 import least_common, most_common, solve_1, solve_2

input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_solve_1():
    assert solve_1(input) == 198


def test_most_common():
    assert most_common(input) == "10111"


def test_least_common():
    assert least_common(input) == "01010"


def test_solve_2():
    assert solve_2(input) == 230
