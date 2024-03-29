from main import file_reader
from main.day_08 import solve_1, solve_2

input = file_reader.read(file_name="day08.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input) == 26


def test_solve_2():
    assert solve_2(input) == 61229
