from main.day_14 import solve_1, solve_2

input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]


def test_solve_1():
    assert solve_1(input) == 1588


def test_solve_2():
    assert solve_2(input) == 2188189693529
