from main.file_reader import read


def solve_1(input: list) -> int:
    x, y = 0, 0
    for line in input:
        command, num = line.split(" ")

        if command == "up":
            y -= int(num)
        elif command == "down":
            y += int(num)
        elif command == "forward":
            x += int(num)

    return x * y


def solve_2(input: list) -> int:
    x, y, aim = 0, 0, 0
    for line in input:
        command, num = line.split(" ")

        if command == "up":
            aim -= int(num)
        elif command == "down":
            aim += int(num)
        elif command == "forward":
            x += int(num)
            y += aim * int(num)

    return x * y


if __name__ == "__main__":
    input = read("day02-01.txt")
    print(solve_1(input))  # 1694130
    print(solve_2(input))  # 1698850445
