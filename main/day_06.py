from main.file_reader import read


def solve_1(input: list) -> int:
    fishes = list(map(int, input[0].split(",")))
    return solve(fishes, 80)


def solve_2(input: list) -> int:
    fishes = list(map(int, input[0].split(",")))
    return solve(fishes, 256)


def solve(fishes: list, days: int) -> int:
    counts = [0] * 9
    for fish in fishes:
        counts[fish] += 1

    for _ in range(days):
        new_counts = [0] * 9
        for i in range(9):
            new_counts[i] = counts[(i + 1) % 9]
        new_counts[6] += counts[0]
        counts = new_counts
    return sum(counts)


if __name__ == "__main__":
    input = read("day06-01.txt")
    print(solve_1(input))  # 395627
    print(solve_2(input))  # 1767323539209
