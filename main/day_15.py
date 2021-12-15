from main.file_reader import read


def solve_1(input: list) -> int:
    return dijkstra(input)


def dijkstra(grid):
    def find_neighbours(row, col):
        ns = []
        if row != 0:
            ns.append((row - 1, col))
        if row != len(grid) - 1:
            ns.append((row + 1, col))
        if col != 0:
            ns.append((row, col - 1))
        if col != len(grid[0]) - 1:
            ns.append((row, col + 1))
        return ns

    q = [(0, 0, 0)]
    costs = {}
    while len(q) > 0:
        cost, row, col = q[0]
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return cost
        q = q[1:]
        for (n_row, n_col) in find_neighbours(row, col):
            new_cost = cost + int(grid[n_row][n_col])
            if (n_row, n_col) not in costs or costs[(n_row, n_col)] > new_cost:
                costs[(n_row, n_col)] = new_cost
                q.append((new_cost, n_row, n_col))
        q.sort()


def solve_2(input: list) -> int:
    new_grid = expand_grid(input)
    return dijkstra(new_grid)


def expand_grid(input):
    num_rows = len(input) * 5
    num_cols = len(input[0]) * 5
    new_grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for row_offset in range(5):
        for col_offset in range(5):
            total_offset = row_offset + col_offset
            for row in range(len(input)):
                for col in range(len(input[0])):
                    new_value = (int(input[row][col]) + total_offset) % 9
                    if new_value == 0:
                        new_value = 9
                    new_grid[row + (row_offset * len(input))][
                        col + (col_offset * len(input[0]))
                    ] = new_value
    return new_grid


if __name__ == "__main__":
    input = read("day15-01.txt")
    print(solve_1(input))  # 366
    print(solve_2(input))  # 2829
