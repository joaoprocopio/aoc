from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


XMASTRIX = []


with open(file_path, "r") as file:
    for line in file:
        XMASTRIX.append([char for char in line.rstrip("\n")])
    print(XMASTRIX)
