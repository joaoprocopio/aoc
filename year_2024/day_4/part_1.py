from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


xmastrix = []
xmascount = 0


with open(file_path, "r") as file:
    for line in file:
        xmastrix.append([char for char in line.rstrip("\n")])

    print(xmascount)
