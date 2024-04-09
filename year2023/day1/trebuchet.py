# https://adventofcode.com/2023/day/1
from pathlib import Path


def trebuchet():
    file = Path(__file__).parent / "trebuchet.txt"
    lines = open(file).read().splitlines()
    total = 0

    for line in lines:
        line_numbers: list[str] = []

        for char in line:
            if not char.isdigit():
                continue

            line_numbers.append(char)

        total += int(line_numbers[0] + line_numbers[-1])

    print(total)


if __name__ == "__main__":
    trebuchet()
