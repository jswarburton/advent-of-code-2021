from main.file_reader import read


def solve_1(input: str) -> int:
    binary = convert(input)
    _, version_total, _ = parse_packets(binary)
    return version_total


def solve_2(input: str) -> int:
    binary = convert(input)
    _, _, value = parse_packets(binary)
    return value


def parse_packets(data, version_total=0):
    version, data = int(data[:3], 2), data[3:]
    version_total += version
    type_id, data = int(data[:3], 2), data[3:]

    if type_id == 4:  # literal value
        binary_rep = ""
        while data[0] == "1":
            binary_rep, data = binary_rep + data[1:5], data[5:]
        binary_rep, data = binary_rep + data[1:5], data[5:]
        literal_value = int(binary_rep, 2)
    else:  # operator
        sub_values = []
        length_type_id, data = data[0], data[1:]
        if length_type_id == "0":
            sub_packet_length, data = int(data[:15], 2), data[15:]
            sub_packets, data = data[:sub_packet_length], data[sub_packet_length:]
            while len(sub_packets) and int(sub_packets, 2):
                sub_packets, version_total, value = parse_packets(sub_packets, version_total)
                sub_values.append(value)
        else:
            num_sub_packets, data = int(data[:11], 2), data[11:]
            for i in range(num_sub_packets):
                data, version_total, value = parse_packets(data, version_total)
                sub_values.append(value)

        if type_id == 0:
            literal_value = sum(sub_values)
        elif type_id == 1:
            literal_value = 1
            for i in sub_values:
                literal_value *= i
        elif type_id == 2:
            literal_value = min(sub_values)
        elif type_id == 3:
            literal_value = max(sub_values)
        elif type_id == 5:
            literal_value = sub_values[0] > sub_values[1]
        elif type_id == 6:
            literal_value = sub_values[0] < sub_values[1]
        elif type_id == 7:
            literal_value = sub_values[0] == sub_values[1]

    return data, version_total, literal_value


def convert(hex: str):
    return (
        hex.replace("0", "0000")
        .replace("1", "0001")
        .replace("2", "0010")
        .replace("3", "0011")
        .replace("4", "0100")
        .replace("5", "0101")
        .replace("6", "0110")
        .replace("7", "0111")
        .replace("8", "1000")
        .replace("9", "1001")
        .replace("A", "1010")
        .replace("B", "1011")
        .replace("C", "1100")
        .replace("D", "1101")
        .replace("E", "1110")
        .replace("F", "1111")
    )


if __name__ == "__main__":
    input = read("day16-01.txt")
    print(solve_1(input[0]))  # 889
    print(solve_2(input[0]))  # 739303923668
