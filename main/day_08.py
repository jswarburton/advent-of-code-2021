from main.file_reader import read


def solve_1(input: list) -> int:
    count = 0
    for line in input:
        first, second = line.split(" | ")
        second_parts = second.split()

        for part in second_parts:
            if len(part) in {2, 3, 4, 7}:
                count += 1

    return count


def solve_2(input: list) -> int:
    totals = []
    for line in input:
        first, second = line.split(" | ")
        first_parts = first.split()
        second_parts = second.split()

        possibles = [set() for _ in range(10)]
        actuals = [""] * 10

        for part in first_parts:
            if len(part) == 2:
                actuals[1] = part
            elif len(part) == 3:
                actuals[7] = part
            elif len(part) == 4:
                actuals[4] = part
            elif len(part) == 7:
                actuals[8] = part
            elif len(part) == 6:
                possibles[0].add(part)
                possibles[6].add(part)
                possibles[9].add(part)
            elif len(part) == 5:
                possibles[2].add(part)
                possibles[3].add(part)
                possibles[5].add(part)

        # 6 doesn't contain all of 1, but 9 and 0 do
        for poss in possibles[6]:
            if not set(actuals[1]).issubset(set(poss)):
                actuals[6] = poss
                possibles[9].remove(poss)
                possibles[0].remove(poss)

        # All of 4 is contained in 9, but 0 isn't
        for poss in possibles[9]:
            if set(actuals[4]).issubset(set(poss)):
                actuals[9] = poss
                possibles[0].remove(poss)
                actuals[0] = list(possibles[0])[0]

        # All of 5 is contained in 6, but not 2 or 3
        for poss in possibles[5]:
            if set(poss).issubset(set(actuals[6])):
                actuals[5] = poss
                possibles[2].remove(poss)
                possibles[3].remove(poss)

        # All of 3 is contained in 9, but not 2
        for poss in possibles[3]:
            if set(poss).issubset(set(actuals[9])):
                actuals[3] = poss
                possibles[2].remove(poss)
                actuals[2] = list(possibles[2])[0]

        total = 0
        for part in second_parts:
            for i in range(10):
                if set(part) == set(actuals[i]):
                    total = total * 10 + i
                    break

        totals.append(total)

    return sum(totals)


if __name__ == "__main__":
    input = read("day08-01.txt")
    print(solve_1(input))  # 416
    print(solve_2(input))  # 1043697
