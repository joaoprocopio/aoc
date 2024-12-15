from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


xmastrix = []
xmascount = 0


XMAS_HORIZONTAL = [
    ["X", "M", "A", "S"],
]
XMAS_HORIZONTAL_REVERSE = [
    ["S", "A", "M", "X"],
]

XMAS_VERTICAL = [
    ["X"],
    ["M"],
    ["A"],
    ["S"],
]
XMAS_VERTICAL_REVERSE = [
    ["S"],
    ["A"],
    ["M"],
    ["X"],
]


XMAS_DIAGONAL_AB = [
    [None, None, None, "X"],
    [None, None, "M"],
    [None, "A"],
    ["S"],
]
XMAS_DIAGONAL_AB_REVERSE = [
    [None, None, None, "S"],
    [None, None, "A"],
    [None, "M"],
    ["X"],
]

XMAS_DIAGONAL_CD = [
    ["X"],
    [None, "M"],
    [None, None, "A"],
    [None, None, None, "S"],
]
XMAS_DIAGONAL_CD_REVERSE = [
    [None, None, None, "S"],
    [None, None, "A"],
    [None, "M"],
    ["X"],
]


with open(file_path, "r") as file:
    for line in file:
        xmastrix.append([char for char in line.rstrip("\n")])

    print(xmascount)
