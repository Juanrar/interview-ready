# 4. *Palindrome Permutation*:

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# ```
# EXAMPLE
# Input: Tact Coa
# Output True (permutations: "taco cat", "atco cta", etc.)
# ```


def palindrome_permutation(s: str) -> bool:
    counts = {}

    for ch in s.lower():
        if ch == " ":
            continue
        counts[ch] = 1 + counts.get(ch, 0)

    odd_count = 0
    for count in counts.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True


# Tests


def test_empty_string():
    assert palindrome_permutation("") is True


def test_single_character_string():
    assert palindrome_permutation("a") is True


def test_palindrome_with_odd_length():
    assert palindrome_permutation("taco cat") is True


def test_palindrome_with_even_length():
    assert palindrome_permutation("rdeder") is True


def test_non_palindrome_with_odd_length():
    assert palindrome_permutation("hello") is False


def test_non_palindrome_with_even_length():
    assert palindrome_permutation("world") is False


def test_string_with_mixed_case():
    assert palindrome_permutation("RaceCar") is True


def test_string_with_repeated_letters():
    assert palindrome_permutation("rrracecrrar") is True


def test_string_with_digits():
    assert palindrome_permutation("12321") is True


def test_string_with_no_possible_palindrome_permutation():
    assert palindrome_permutation("abcdefg") is False
