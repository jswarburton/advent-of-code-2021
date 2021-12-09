from collections import deque

from main.file_reader import read


def solve_1(input: list) -> int:
    low_points = []

    for row, line in enumerate(input):
        for col, entry in enumerate(line):
            neighbours = find_neighbours(row, col, len(input) - 1, len(input[0]) - 1)
            if all(int(entry) < int(input[nr][nc]) for (nr, nc) in neighbours):
                low_points.append(int(line[col]))

    return sum(low_points) + len(low_points)


def solve_2(input: list) -> int:
    basin_sizes = []
    seen_points = set()

    for row in range(len(input)):
        for col in range(len(input[0])):
            if (row, col) not in seen_points and int(input[row][col]) != 9:
                size = 0
                queue = deque()
                queue.append((row, col))
                while queue:
                    (row, col) = queue.popleft()
                    if (row, col) in seen_points:
                        continue
                    seen_points.add((row, col))
                    size += 1
                    for (nr, nc) in find_neighbours(row, col, len(input) - 1, len(input[0]) - 1):
                        if int(input[nr][nc]) != 9:
                            queue.append((nr, nc))
                basin_sizes.append(size)
    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def find_neighbours(row, col, max_row, max_col):
    ns = []

    if row != 0:
        ns.append((row - 1, col))
    if row != max_row:
        ns.append((row + 1, col))
    if col != 0:
        ns.append((row, col - 1))
    if col != max_col:
        ns.append((row, col + 1))

    return ns


if __name__ == "__main__":
    input = read("day09-01.txt")
    print(solve_1(input))  # 526
    print(solve_2(input))  # 1123524
