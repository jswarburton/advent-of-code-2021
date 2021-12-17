from main.file_reader import read


def solve_1(input: str) -> int:
    max_y_position, _ = solve(input)
    return max_y_position


def solve_2(input: str) -> int:
    _, num_valid_starting_velocities = solve(input)
    return num_valid_starting_velocities


def solve(input: str) -> (int, int):
    xs, ys = input[15:].split(", y=")

    x_min, x_max = map(int, xs.split(".."))
    y_min, y_max = map(int, ys.split(".."))

    def loop(x_vel, y_vel):
        x, y = 0, 0
        max_y_pos = -99999999999

        while y >= y_min:
            max_y_pos = max(max_y_pos, y)
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return max_y_pos

            x += x_vel
            y += y_vel

            y_vel -= 1
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1

        return None

    max_points = []
    valid_starting_vels = set()

    for starting_x_vel in range(1, x_max + 1):
        for starting_y_vel in range(y_min, -y_min + 1):
            max_y_pos = loop(starting_x_vel, starting_y_vel)
            if max_y_pos is not None:
                max_points.append(max_y_pos)
                valid_starting_vels.add((starting_x_vel, starting_y_vel))

    return max(max_points), len(valid_starting_vels)


if __name__ == "__main__":
    input = read("day17-01.txt")[0]
    print(solve_1(input))  # 7626
    print(solve_2(input))  # 2032
