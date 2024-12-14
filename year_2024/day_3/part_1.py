import tokenize
from collections import deque
from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


# mul   = len(3)        3
# (     = len(1)        4
# X     = len(1 -> 3)   7
# ,     = len(1)        8
# Y     = len(1 -> 3)   11
# )     = len(1)        12

with tokenize.open(file_path) as file:
    tokens = tokenize.generate_tokens(file.readline)
    stack = deque()

    for token in tokens:
        match token:
            case tokenize.TokenInfo(type=tokenize.NAME, string="mul"):
                print(token)
            case tokenize.TokenInfo(type=tokenize.NUMBER):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string="("):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string=","):
                pass
            case tokenize.TokenInfo(type=tokenize.OP, string=")"):
                pass
