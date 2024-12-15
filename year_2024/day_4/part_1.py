from pathlib import Path

dir_path = Path(__file__).parent
file_path = dir_path / "sample.txt"


XMAS = "XMAS"

with open(file_path, "r") as file:
    for line in file:
        print(line)
