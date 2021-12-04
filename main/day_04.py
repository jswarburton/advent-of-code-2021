from main.file_reader import read


def solve_1(input: list) -> int:
    numbers = input[0].split(",")
    boards = parse_boards(input[2:])

    for num in numbers:
        for board in boards:
            for line in board:
                for i, board_num in enumerate(line):
                    if num == board_num:
                        line[i] = "X"

            if is_winner(board):
                return sum_all_numeric_entries(board) * int(num)


def is_winner(board):
    for line in board:
        if all(c == "X" for c in line):
            return True

    for i in range(5):
        if all(line[i] == "X" for line in board):
            return True

    return False


def sum_all_numeric_entries(board):
    return sum(int(i) for line in board for i in line if i.isnumeric())


def parse_boards(lines: list) -> list:
    boards = []

    current_board = []
    for line in lines:
        if not line:
            boards.append(current_board)
            current_board = []
        else:
            current_board.append(line.split())
    boards.append(current_board)

    return boards


def solve_2(input: list) -> int:
    numbers = input[0].split(",")
    boards = parse_boards(input[2:])

    winning_boards = set()

    for num in numbers:
        for board_idx, board in enumerate(boards):
            if board_idx in winning_boards:
                continue

            for line in board:
                for i, board_num in enumerate(line):
                    if num == board_num:
                        line[i] = "X"

            if is_winner(board):
                winning_boards.add(board_idx)
                if len(winning_boards) == len(boards):
                    return sum_all_numeric_entries(board) * int(num)


if __name__ == "__main__":
    input = read("day04-01.txt")
    print(solve_1(input))  # 34506
    print(solve_2(input))  # 7686
