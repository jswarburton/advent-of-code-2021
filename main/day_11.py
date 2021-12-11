from main.file_reader import read


def solve_1(input: list) -> int:
    input = [list(map(int, list(row))) for row in input]

    flashes = 0
    for i in range(100):
        input = step(input)
        flashes += sum(1 for row in input for entry in row if entry == 0)

    return flashes


def step(input):
    flashed = set()

    def flash(row, col):
        flashed.add((row, col))
        neighbours = find_neighbours(row, col, len(input) - 1, len(input[0]) - 1)
        for (neighbour_row, neighbour_col) in neighbours:
            input[neighbour_row][neighbour_col] += 1
            if (neighbour_row, neighbour_col) not in flashed and input[neighbour_row][
                neighbour_col
            ] > 9:
                flash(neighbour_row, neighbour_col)

    for row in range(len(input)):
        for col in range(len(input[0])):
            input[row][col] += 1
            if input[row][col] == 10:
                flash(row, col)

    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] >= 10:
                input[row][col] = 0

    return input


def solve_2(input: list) -> int:
    input = [list(map(int, list(row))) for row in input]

    steps = 0
    while not all(entry == 0 for row in input for entry in row):
        input = step(input)
        steps += 1
    return steps


def find_neighbours(row, col, max_row, max_col):
    ns = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
    return [
        (n_row, n_col)
        for (n_row, n_col) in ns
        if 0 <= n_row <= max_row and 0 <= n_col <= max_col and (n_row, n_col) != (row, col)
    ]


if __name__ == "__main__":
    input = read("day11-01.txt")
    print(solve_1(input))  # 1637
    print(solve_2(input))  # 242
