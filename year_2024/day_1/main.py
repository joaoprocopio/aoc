from pathlib import Path

dir = Path(__file__).parent
input = dir / "sample.txt"
file = open(input)

print(file.read())
