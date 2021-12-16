from main.day_16 import solve_1, solve_2


def test_solve_1():
    assert solve_1("8A004A801A8002F478") == 16
    assert solve_1("620080001611562C8802118E34") == 12
    assert solve_1("C0015000016115A2E0802F182340") == 23
    assert solve_1("A0016C880162017C3686B18A3D4780") == 31


def test_solve_2():
    assert solve_2("C200B40A82") == 3
    assert solve_2("04005AC33890") == 54
    assert solve_2("880086C3E88112") == 7
    assert solve_2("CE00C43D881120") == 9
    assert solve_2("D8005AC2A8F0") == 1
    assert solve_2("F600BC2D8F") == 0
    assert solve_2("9C005AC2F8F0") == 0
    assert solve_2("9C0141080250320F1802104A08") == 1
