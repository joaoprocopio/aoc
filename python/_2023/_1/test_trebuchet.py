from pathlib import Path

from _2023._1.trebuchet import trebuchet

dir = Path(__file__).parent
file = dir / "trebuchet.txt"


def test_trebuchet():
    text = open(file).read()
    lines = text.splitlines()

    assert trebuchet(lines) == 53386
