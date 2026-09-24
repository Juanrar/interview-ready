# 2. *Robot in a Grid*:

# Imagine a robot sitting on the upper left corner of a grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are
# "off limits" such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the bottom right.
#
# grid[row][col] is True when the robot can step on that cell.
# Return the path as a list of (x, y) tuples, where x is the column and y is the row,
# or False if there is no path.

from typing import Literal

Grid = list[list[bool]]
Path = list[tuple[int, int]]


def robot_in_a_grid(grid: Grid) -> Path | Literal[False]:
    pass


# Tests


def test_returns_path_for_3x3_grid():
    grid = [
        [True, True, False],
        [True, False, True],
        [True, True, True],
    ]
    assert robot_in_a_grid(grid) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]


def test_returns_path_for_4x4_grid():
    grid = [
        [True, True, True, False],
        [True, False, True, True],
        [True, True, False, False],
        [False, True, True, True],
    ]
    assert robot_in_a_grid(grid) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (3, 3),
    ]


def test_returns_false_when_there_is_no_path():
    grid = [
        [True, False, True, False],
        [False, False, True, True],
        [True, True, True, False],
        [True, True, True, True],
    ]
    assert robot_in_a_grid(grid) is False
