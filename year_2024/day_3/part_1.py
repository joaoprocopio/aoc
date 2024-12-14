from pathlib import Path
from tokenize import tokenize

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


MUL: str = "mul"
OPEN_PAREN: str = "("
CLOSED_PAREN: str = ")"
COMMA: str = ","

MUL_OPEN_PAREN = MUL + OPEN_PAREN
MUL_OPEN_PAREN_LEN = len(MUL) + len(OPEN_PAREN)

with open(file_path, "rb") as file:
    tokens = tokenize(file.readline)

    for token in tokens:
        print(token.string)
