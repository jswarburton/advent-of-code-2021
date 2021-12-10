from main.file_reader import read


def solve_1(input: list) -> int:
    total_score = 0

    for line in input:
        stack = []
        for c in line:
            if c in {"(", "[", "{", "<"}:
                stack.append(c)
            elif c == ")":
                if stack.pop() != "(":
                    total_score += 3
                    break
            elif c == "]":
                if stack.pop() != "[":
                    total_score += 57
                    break
            elif c == "}":
                if stack.pop() != "{":
                    total_score += 1197
                    break
            elif c == ">":
                if stack.pop() != "<":
                    total_score += 25137
                    break

    return total_score


def solve_2(input: list) -> int:
    corrupt_lines = set()
    scores = []
    for line in input:
        stack = []

        for c in line:
            if c in {"(", "[", "{", "<"}:
                stack.append(c)
            elif c == ")":
                if stack.pop() != "(":
                    corrupt_lines.add(line)
                    break
            elif c == "]":
                if stack.pop() != "[":
                    corrupt_lines.add(line)
                    break
            elif c == "}":
                if stack.pop() != "{":
                    corrupt_lines.add(line)
                    break
            elif c == ">":
                if stack.pop() != "<":
                    corrupt_lines.add(line)
                    break

    incomplete_lines = [line for line in input if line not in corrupt_lines]

    for line in incomplete_lines:
        stack = []

        for c in line:
            if c in {"(", "[", "{", "<"}:
                stack.append(c)
            elif c == ")":
                if stack.pop() != "(":
                    break
            elif c == "]":
                if stack.pop() != "[":
                    break
            elif c == "}":
                if stack.pop() != "{":
                    break
            elif c == ">":
                if stack.pop() != "<":
                    break
        score = 0
        for c in reversed(stack):
            if c == "(":
                score = (score * 5) + 1
            elif c == "[":
                score = (score * 5) + 2
            elif c == "{":
                score = (score * 5) + 3
            elif c == "<":
                score = (score * 5) + 4
        scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    input = read("day10-01.txt")
    print(solve_1(input))  # 323613
    print(solve_2(input))  # 3103006161
