# 5. *One Away*:

# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.


def is_one_away(s1: str, s2: str) -> bool:
    pass


# Tests


def test_replace():
    assert is_one_away("pale", "bale") is True
    assert is_one_away("bbaa", "bcca") is False


def test_insert():
    assert is_one_away("pale", "ple") is True


def test_remove():
    assert is_one_away("pale", "pales") is True


def test_same_strings():
    assert is_one_away("abc", "abc") is True


def test_more_than_one_edit_away():
    assert is_one_away("abcd", "efgh") is False


def test_more_than_one_edit_away_2():
    assert is_one_away("palesa", "pale") is False


def test_empty_strings():
    assert is_one_away("", "") is True


def test_one_character_difference():
    assert is_one_away("a", "ab") is True


def test_empty_and_non_empty_string():
    assert is_one_away("", "a") is True
