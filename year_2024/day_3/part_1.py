import tokenize
from dataclasses import dataclass
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"


MUL_SYMBOL = "MUL"
L_PAREN_SYMBOL = "L_PAREN"
X_VALUE_SYMBOL = "X_VALUE"
COMMA_SYMBOL = "COMMA"
Y_VALUE_SYMBOL = "Y_VALUE"
R_PAREN_SYMBOL = "R_PAREN"


@dataclass
class MUL_INSTRUCTION:
    MUL: str
    L_PAREN: str
    X_VALUE: int
    COMMA: str
    Y_VALUE: int
    R_PAREN: str


with open(file_path, "rb") as file:
    tokens = tokenize.tokenize(file.readline)
    total = 0

    instructions = dict()

    for token in tokens:
        match token:
            case tokenize.TokenInfo(type=tokenize.NAME) if token.string.endswith("mul"):
                pass
            case tokenize.TokenInfo(type=tokenize.NUMBER):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string="("):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string=","):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string=")"):
                pass
