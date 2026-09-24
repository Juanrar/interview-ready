# 3. *Magic Index*:

# A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.

# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# FOLLOW UP: What if the values are not distinct?

from typing import Optional


def find_magic_index_distinct(arr: list[int]) -> Optional[int]:
    pass


def find_magic_index_non_distinct(arr: list[int]) -> Optional[int]:
    pass


# Tests


def test_returns_magic_index_for_distinct_input():
    assert find_magic_index_distinct([-2, -1, 0, 2, 4, 6, 8]) == 4


def test_returns_none_when_distinct_input_has_no_magic_index():
    assert find_magic_index_distinct([-3, -2, -1, 4, 5, 7, 9]) is None


def test_returns_magic_index_for_non_distinct_input():
    assert find_magic_index_non_distinct([-10, -5, 2, 2, 2, 2, 4, 7, 9, 12, 13]) == 2


def test_returns_none_when_non_distinct_input_has_no_magic_index():
    assert find_magic_index_non_distinct([-10, -5, 0, 2, 5, 7, 9, 12, 13]) is None
