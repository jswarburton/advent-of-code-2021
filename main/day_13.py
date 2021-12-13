from main.file_reader import read


def solve_1(input: list) -> int:
    coords, folds = _parse_coords_and_folds(input)
    coords = _fold(coords, folds[:1])
    return len(coords)


def _parse_coords_and_folds(input):
    process_folds = False
    coords = []
    folds = []
    for line in input:
        if not process_folds and line:
            x, y = list(map(int, line.split(",")))
            coords.append((x, y))
        elif not line:
            process_folds = True
        else:
            a, b = line[11:].split("=")
            folds.append((a, int(b)))
    return coords, folds


def solve_2(input: list):
    coords, folds = _parse_coords_and_folds(input)
    coords = _fold(coords, folds)
    _print_grid(coords)


def _fold(coords, folds):
    for fold_dim, fold_val in folds:
        new_coords = set()
        for x, y in coords:
            if fold_dim == "x":
                if x < fold_val:
                    new_coords.add((x, y))
                elif x == fold_val:
                    continue
                else:
                    new_coords.add((fold_val - (x - fold_val), y))
            else:
                if y < fold_val:
                    new_coords.add((x, y))
                elif y == fold_val:
                    continue
                else:
                    new_coords.add((x, fold_val - (y - fold_val)))
        coords = new_coords
    return coords


def _print_grid(coords):
    min_x, min_y = 9999999, 9999999
    max_x, max_y = 0, 0
    for (x, y) in coords:
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if x == min_x:
                print()
            if (x, y) in coords:
                print("x", end="")
            else:
                print(".", end="")


if __name__ == "__main__":
    input = read("day13-01.txt")
    print(solve_1(input))  # 720
    solve_2(input)  # AHPRPAUZ (See visual output)
