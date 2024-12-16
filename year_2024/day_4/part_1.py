from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


count = 0


matrix = []
matrix_rows_len = 0
matrix_cols_len = 0


XMAS = "XMAS"
XMAS_HORIZONTAL = [
    (0, 0, XMAS[0]),
    (0, 1, XMAS[1]),
    (0, 2, XMAS[2]),
    (0, 3, XMAS[3]),
]


"""
se encontrar um X:
- horizontal
    - posição (0, 0) é igual a X
    - posição (0, 1) é igual a M
    - posição (0, 2) é igual a A
    - posição (0, 3) é igual a S
- vertical
    - posição (0, 0,) é igual a X
    - posição (1, 0,) é igual a M
    - posição (2, 0,) é igual a A
    - posição (3, 0,) é igual a S
- diagonal 45°
- diagonal 135°
- diagonal 225°
- diagonal 315°
"""


with open(file_path, "r") as file:
    for line in file:
        matrix.append([char for char in line.rstrip("\n")])

    matrix_rows_len = len(matrix)
    matrix_cols_len = len(matrix[0])

    rows_index = 0

    while rows_index < matrix_rows_len:
        cols_index = 0

        while cols_index < matrix_cols_len:
            print(matrix[rows_index][cols_index])
            cols_index += 1

        rows_index += 1
