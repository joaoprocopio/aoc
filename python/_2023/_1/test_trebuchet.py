from pathlib import Path

from _2023._1.trebuchet import trebuchet_1

dir = Path(__file__).parent
file = dir / "trebuchet.txt"
text = open(file).read()
lines = text.splitlines()


def test_trebuchet_1():
    assert trebuchet_1(lines) == 55971
