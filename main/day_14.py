from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input, 10)


def solve_2(input: list) -> int:
    return solve(input, 40)


def solve(input: list, iterations: int) -> int:
    template = input[0]

    rules = dict()
    for line in input[2:]:
        a, b = line.split(" -> ")
        rules[a] = b

    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[template[i : i + 2]] += 1

    for _ in range(iterations):
        new_pair_counts = defaultdict(int)

        for pair, count in pair_counts.items():
            if pair in rules:
                new_pair_counts[pair[0] + rules[pair]] += count
                new_pair_counts[rules[pair] + pair[1]] += count
            else:
                new_pair_counts[pair] += count

        pair_counts = new_pair_counts

    counts = defaultdict(int)
    for pair, count in pair_counts.items():
        counts[pair[0]] += count
    counts[template[-1]] += 1

    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    input = read("day14-01.txt")
    print(solve_1(input))  # 3406
    print(solve_2(input))  # 3941782230241
