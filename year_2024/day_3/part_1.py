import tokenize
from dataclasses import dataclass
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "input.txt"

MUL_SYMBOL: str = "MUL"
L_PAREN_SYMBOL: str = "L_PAREN"
X_VALUE_SYMBOL: str = "X_VALUE"
COMMA_SYMBOL: str = "COMMA"
Y_VALUE_SYMBOL: str = "Y_VALUE"
R_PAREN_SYMBOL: str = "R_PAREN"


@dataclass
class MulInstruction:
    MUL: str
    L_PAREN: str
    X_VALUE: int
    COMMA: str
    Y_VALUE: int
    R_PAREN: str


# mul   = len(3)        3
# (     = len(1)        4
# X     = len(max. 3)   7
# ,     = len(1)        8
# Y     = len(max. 3)   11
# )     = len(1)        12

with tokenize.open(file_path) as file:
    tokens = tokenize.generate_tokens(file.readline)
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
