# 2. *Check Permutation*:

# Given two strings, write a method to decide if one is a permutation of the other.


def check_permutations(s1: str, s2: str) -> bool:
    #return sorted(s1) == sorted(s2) 
    def counting(s):
        result = {}
        for c in s:
            result[c] = 1 + result.get(c, 0)
        #print("result: ", result)
        return result
    return counting(s2) == counting(s1)


# Tests


def test_returns_true_for_permutations_with_same_length():
    assert check_permutations("abc", "cba") is True


def test_returns_false_for_different_lengths():
    assert check_permutations("abc", "cbad") is False


def test_returns_true_for_permutations_with_special_characters():
    assert check_permutations("abc!", "!bac") is True


def test_returns_false_for_non_permutations_with_special_characters():
    assert check_permutations("abc!", "!bcd") is False


def test_returns_true_for_empty_strings():
    assert check_permutations("", "") is True


def test_returns_true_for_long_strings_with_same_characters():
    assert check_permutations("a" * 1000, "a" * 1000) is True


def test_returns_false_for_long_strings_with_different_characters():
    assert check_permutations("a" * 1000, "b" * 1000) is False
