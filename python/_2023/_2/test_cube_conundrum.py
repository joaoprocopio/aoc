from pathlib import Path

from _2023._2.cube_conundrum import cube_conundrum_1

file = Path(__file__).parent / "cube_conundrum.txt"
lines = open(file).read().splitlines()


def test_cube_conundrum_1():
    assert cube_conundrum_1(lines) is None
