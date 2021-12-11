from main.day_11 import solve_1, solve_2

input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


def test_solve_1():
    assert solve_1(input) == 1656


def test_solve_2():
    assert solve_2(input) == 195
