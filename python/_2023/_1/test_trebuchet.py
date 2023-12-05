from pathlib import Path

from _2023._1.trebuchet import trebuchet_1, trebuchet_2

dir = Path(__file__).parent
file = dir / "trebuchet.txt"
text = open(file).read()
lines = text.splitlines()


def test_trebuchet_1():
    assert trebuchet_1(lines) == 55971


def test_trebuchet_2():
    assert trebuchet_2(lines) == 54719
