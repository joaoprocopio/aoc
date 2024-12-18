from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


class XmasChar:
    X = "X"
    M = "M"
    A = "A"
    S = "S"


XMAS = "XMAS"

UP: tuple[int, int] = (-1, 0)
DOWN: tuple[int, int] = (1, 0)
LEFT: tuple[int, int] = (0, -1)
RIGHT: tuple[int, int] = (0, 1)
LEFT_UP: tuple[int, int] = (-1, -1)
LEFT_DOWN: tuple[int, int] = (1, -1)
RIGHT_UP: tuple[int, int] = (-1, 1)
RIGHT_DOWN: tuple[int, int] = (1, 1)

DIRECTIONS: list[tuple[int, int]] = [
    UP,
    DOWN,
    LEFT,
    RIGHT,
    LEFT_UP,
    LEFT_DOWN,
    RIGHT_UP,
    RIGHT_DOWN,
]


with open(file_path, "r") as file:
    count: int = 0

    matrix: list[list[str]] = []
    matrix_rows_len: int = 0
    matrix_cols_len: int = 0

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
