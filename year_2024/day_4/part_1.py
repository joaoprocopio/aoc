from pathlib import Path
from typing import Optional

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"

abc = Optional

count = 0


matrix: list[list[str]] = []
matrix_rows_len: int = 0
matrix_cols_len: int = 0


XMAS = "XMAS"
DIRECTIONS = []

"""
( 1, -1) | ( 1,  0) | ( 1, 1)
( 0, -1) | ( 0,  0) | ( 0, 1)
(-1, -1) | (-1,  0) | (-1, 1)
"""


"""
se encontrar um X:
- horizontal
    - posição (0, 0) é igual a X
    - posição (0, 1) é igual a M
    - posição (0, 2) é igual a A
    - posição (0, 3) é igual a S
- vertical
    - posição (0, 0) é igual a X
    - posição (1, 0) é igual a M
    - posição (2, 0) é igual a A
    - posição (3, 0) é igual a S
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

    row_index = 0

    while row_index < matrix_rows_len:
        col_index = 0

        while col_index < matrix_cols_len:
            char = matrix[row_index][col_index]

            if char == XMAS[0]:
                for next_row_index, next_col_index, desired_char in XMAS_HORIZONTAL:
                    desired_row_index = row_index + next_row_index
                    desired_col_index = col_index + next_col_index

                    if not (
                        desired_row_index < matrix_rows_len
                        and desired_col_index < matrix_cols_len
                    ):
                        break

                    curr_char = matrix[desired_row_index][desired_col_index]

                    if not curr_char == desired_char:
                        break

                    print(curr_char)

            col_index += 1

        row_index += 1
