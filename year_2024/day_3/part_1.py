import tokenize
from dataclasses import dataclass
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


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

    instruction = dict()

    for token in tokens:
        match token:
            case tokenize.TokenInfo(type=tokenize.NAME) if token.string.endswith("mul"):
                instruction["MUL"] = "mul"
            case tokenize.TokenInfo(type=tokenize.NUMBER):
                if instruction.get("COMMA") == ",":
                    instruction["Y_VALUE"] = int(token.string)
                else:
                    instruction["X_VALUE"] = int(token.string)
            case tokenize.TokenInfo(type=tokenize.OP, string="("):
                instruction["L_PAREN"] = "("
            case tokenize.TokenInfo(type=tokenize.OP, string=","):
                instruction["COMMA"] = ","
            case tokenize.TokenInfo(type=tokenize.OP, string=")"):
                instruction["R_PAREN"] = ")"

                try:
                    instruction = MUL_INSTRUCTION(**instruction)
                    total += instruction.X_VALUE * instruction.Y_VALUE
                    print(instruction)
                    instruction = dict()
                except Exception:
                    instruction = dict()
    print(total)
