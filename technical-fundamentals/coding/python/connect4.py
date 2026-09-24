"""
Connect4

Connect4 is a game where two players take turns placing a token on columns that drop to the bottom.
When a player forms 4 of his tokens in a line - horizontally, vertically, or diagonally - the player wins.

[Visualization](https://i.ebayimg.com/images/g/DzMAAOSwSjxj6m0e/s-l1600.jpg)

Implement Connect 4 with the class below.

- Rows and columns start at 1. Row 1 is the top row and row `height` is the bottom row.
- PLAYER_ONE plays first.
- Plays outside the board are ignored.
- Once there is a winner, further plays are ignored.
"""

from typing import Optional

PLAYER_ONE = 1
PLAYER_TWO = 2


class Connect4:
    def __init__(self, width: int = 7, height: int = 6):
        pass

    def play(self, col: int) -> None:
        pass

    def get_value(self, row: int, col: int) -> Optional[int]:
        """Returns the player in that cell, or None if it is empty or out of bounds."""
        pass

    def winner(self) -> Optional[int]:
        pass

    def print(self) -> None:
        pass


# Tests


def test_allows_plays_within_bounds():
    c4 = Connect4(width=10, height=10)
    assert not c4.get_value(10, 1)
    c4.play(1)
    assert c4.get_value(10, 1) == PLAYER_ONE


def test_players_alternate_turns():
    c4 = Connect4(width=10, height=10)
    c4.play(1)
    c4.play(1)
    assert c4.get_value(10, 1) == PLAYER_ONE
    assert c4.get_value(9, 1) == PLAYER_TWO


def test_ignores_plays_out_of_bounds():
    c4 = Connect4(width=10, height=10)
    c4.play(100)
    assert not c4.get_value(100, 1)


def test_no_winner_at_start():
    c4 = Connect4(width=10, height=10)
    assert c4.winner() is None


def test_detects_horizontal_win():
    c4 = Connect4(width=10, height=10)
    for col in range(1, 5):
        c4.play(col)
        c4.play(col)
    assert c4.winner() == PLAYER_ONE


def test_detects_vertical_win():
    c4 = Connect4(width=10, height=10)
    for _ in range(4):
        c4.play(1)
        c4.play(2)
    assert c4.winner() == PLAYER_ONE


def test_detects_diagonal_win():
    c4 = Connect4(width=10, height=10)
    for col in [1, 2, 2, 3, 4, 3, 3, 4, 5, 4, 4]:
        c4.play(col)
    assert c4.winner() == PLAYER_ONE


def test_detects_win_with_reversed_plays():
    c4 = Connect4(width=10, height=10)
    for col in reversed([1, 2, 2, 3, 4, 3, 3, 4, 5, 4, 4]):
        c4.play(col)
    assert c4.winner() == PLAYER_ONE
