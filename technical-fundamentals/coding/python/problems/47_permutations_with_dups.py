# 7. *Permutations without Dups*: Write a method to compute all permutations of a string of unique characters.


def permutations_without_dups(s: str) -> list[str]:
    pass


# *Permutations with Dups*: Write a method to compute all permutations of a string
# whose characters are not necessarily unique. The list of permutations should not have duplicates.


def permutations_with_dups(s: str) -> list[str]:
    pass


# Tests


def test_permutations_without_dups():
    result = permutations_without_dups("abc")
    assert sorted(result) == ["abc", "acb", "bac", "bca", "cab", "cba"]


def test_permutations_with_dups_of_length_3():
    result = permutations_with_dups("aab")
    assert sorted(result) == ["aab", "aba", "baa"]


def test_permutations_with_dups_of_length_4():
    result = permutations_with_dups("aabb")
    assert sorted(result) == ["aabb", "abab", "abba", "baab", "baba", "bbaa"]
