from pathlib import Path

from _2023._2.cube_conundrum import cube_conundrum

dir = Path(__file__).parent
file = dir / "trebuchet.txt"


def test_cube_conundrum():
    assert cube_conundrum() is None
