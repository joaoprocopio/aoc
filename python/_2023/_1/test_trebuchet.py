from pathlib import Path

from _2023._1.trebuchet import trebuchet_1, trebuchet_2

file = Path(__file__).parent / "trebuchet.txt"
lines = open(file).read().splitlines()


def test_trebuchet_1():
    assert trebuchet_1(lines) == 55971


def test_trebuchet_2():
    assert trebuchet_2(lines) == 54719
