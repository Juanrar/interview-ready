# 6. *Towers of Hanoi*:

# In the classic problem of the Towers of Hanoi, you have 3 towers and
# N disks of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom
# (i.e., each disk sits on top of an even larger one).
#
# You have the following constraints:
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.
#
# Each tower is a list used as a stack: the last element is the top disk.

Tower = list[int]


def towers_of_hanoi(n: int) -> list[Tower]:
    pass


# Tests


def test_moves_all_disks_to_the_last_tower():
    assert towers_of_hanoi(3) == [[], [], [3, 2, 1]]
    assert towers_of_hanoi(4) == [[], [], [4, 3, 2, 1]]
    assert towers_of_hanoi(5) == [[], [], [5, 4, 3, 2, 1]]
