from collections import Counter, defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    connections = defaultdict(list)
    for line in input:
        start, end = line.split("-")
        connections[start].append(end)
        connections[end].append(start)

    paths = []

    def search(path):
        pos = path[-1]
        if pos == "end":
            paths.append(path)
            return
        for n in connections[pos]:
            if n == "start":
                continue
            if not (n.islower() and n in path):
                search(path + [n])

    search(["start"])
    return len(paths)


def is_visitable(path):
    c = Counter([p for p in path if p.islower()])
    return all(v <= 1 for v in c.values())


def solve_2(input: list) -> int:
    connections = defaultdict(list)
    for line in input:
        start, end = line.split("-")
        connections[start].append(end)
        connections[end].append(start)

    paths = []

    def search(path):
        pos = path[-1]
        if pos == "end":
            paths.append(path)
            return
        for n in connections[pos]:
            if n == "start":
                continue
            if not n.islower() or n not in path or is_visitable(path):
                search(path + [n])

    search(["start"])
    return len(paths)


if __name__ == "__main__":
    input = read("day12-01.txt")
    print(solve_1(input))  # 3679
    print(solve_2(input))  # 107395
