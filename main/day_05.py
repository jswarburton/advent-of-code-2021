from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    points = defaultdict(int)

    for line in input:
        a, b = line.split(" -> ")
        x1, y1 = map(int, a.split(","))
        x2, y2 = map(int, b.split(","))

        if x1 == x2 or y1 == y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    points[(x, y)] += 1

    return sum(v >= 2 for v in points.values())


def solve_2(input: list) -> int:
    points = defaultdict(int)

    for line in input:
        a, b = line.split(" -> ")
        x1, y1 = map(int, a.split(","))
        x2, y2 = map(int, b.split(","))

        if x1 == x2 or y1 == y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    points[(x, y)] += 1
        else:
            a = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            b = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for x, y in zip(a, b):
                points[(x, y)] += 1

    return sum(v >= 2 for v in points.values())


if __name__ == "__main__":
    input = read("day05-01.txt")
    print(solve_1(input))  # 7473
    print(solve_2(input))  # 24164
