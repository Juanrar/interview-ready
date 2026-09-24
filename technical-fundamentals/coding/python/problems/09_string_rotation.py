# 9. *String Rotation*:

# Assume you have a method is_substring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring.
# (e.g., "waterbottle" is a rotation of "erbottlewat")

import pytest

_is_substring_called = False


def is_substring(s1: str, s2: str) -> bool:
    """Returns True if s1 contains s2. It can only be called once."""
    global _is_substring_called
    if _is_substring_called:
        raise RuntimeError("is_substring() can be used only once.")
    _is_substring_called = True
    return s2 in s1


def string_rotation(s1: str, s2: str) -> bool:
    pass


# Tests


@pytest.fixture(autouse=True)
def reset_is_substring():
    global _is_substring_called
    _is_substring_called = False


def test_rotates_a_string():
    assert string_rotation("Hello", "oHell") is True


def test_rotates_another_string():
    assert string_rotation("waterbottle", "erbottlewat") is True
