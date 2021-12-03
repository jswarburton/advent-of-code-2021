from main.file_reader import read


def solve_1(input: list) -> int:
    gamma, epsilon = "", ""
    for i in range(len(input[0])):
        chars_at_idx = [line[i] for line in input]

        zeros, ones = 0, 0

        for char in chars_at_idx:
            if char == "0":
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def solve_2(input: list) -> int:
    return int(most_common(input), 2) * int(least_common(input), 2)


def most_common(candidates):
    while len(candidates) != 1:
        for i in range(len(candidates[0])):
            a = [line[i] for line in candidates]

            zeros, ones = 0, 0
            indices_with_zeros = []
            indices_with_ones = []

            for j, char in enumerate(a):
                if char == "0":
                    zeros += 1
                    indices_with_zeros.append(j)
                else:
                    ones += 1
                    indices_with_ones.append(j)

            if ones >= zeros:
                candidates = [candidates[i] for i in indices_with_ones]
            else:
                candidates = [candidates[i] for i in indices_with_zeros]

    return candidates[0]


def least_common(candidates):
    while len(candidates) != 1:
        for i in range(len(candidates[0])):
            a = [line[i] for line in candidates]

            zeros, ones = 0, 0
            indices_with_zeros = []
            indices_with_ones = []

            for j, char in enumerate(a):
                if char == "0":
                    zeros += 1
                    indices_with_zeros.append(j)
                else:
                    ones += 1
                    indices_with_ones.append(j)

            if ones >= zeros:
                candidates = [candidates[i] for i in indices_with_zeros]
            else:
                candidates = [candidates[i] for i in indices_with_ones]

            if len(candidates) == 1:
                return candidates[0]

    return candidates[0]


if __name__ == "__main__":
    input = read("day03-01.txt")
    print(solve_1(input))  # 3923414
    print(solve_2(input))  # 5852595
