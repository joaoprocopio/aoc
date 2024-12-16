from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


xmastrix = []
xmascount = 0


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
        xmastrix.append([char for char in line.rstrip("\n")])

    # print(xmascount)
