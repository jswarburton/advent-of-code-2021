from main.file_reader import read


def solve_1(input: list) -> int:
    positions = list(map(int, input[0].split(",")))

    min_alignment = 99999999999999

    for pos in range(min(positions), max(positions) + 1):
        alignment_cost = sum(abs(pos2 - pos) for pos2 in positions)
        min_alignment = min(alignment_cost, min_alignment)

    return min_alignment


def solve_2(input: list) -> int:
    positions = list(map(int, input[0].split(",")))

    min_alignment = 9999999999999

    for pos in range(min(positions), max(positions) + 1):
        alignment_cost = sum((abs(pos2 - pos) * (abs(pos2 - pos) + 1)) // 2 for pos2 in positions)
        min_alignment = min(alignment_cost, min_alignment)

    return min_alignment


if __name__ == "__main__":
    input = read("day07-01.txt")
    print(solve_1(input))  # 343605
    print(solve_2(input))  # 96744904
