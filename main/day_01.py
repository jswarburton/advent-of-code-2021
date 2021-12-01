from main.file_reader import read


def solve_1(input: list) -> int:
    return count_num_increases([int(i) for i in input])


def count_num_increases(ints: list) -> int:
    return sum(1 for i in range(1, len(ints)) if ints[i] > ints[i - 1])


def solve_2(input: list) -> int:
    ints = [int(i) for i in input]
    windowed = [ints[i] + ints[i - 1] + ints[i - 2] for i in range(2, len(ints))]
    return count_num_increases(windowed)


if __name__ == "__main__":
    input = read("day01-01.txt")
    print(solve_1(input))  # 1184
    print(solve_2(input))  # 1158
