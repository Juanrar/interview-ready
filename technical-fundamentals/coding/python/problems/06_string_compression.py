# 6. *String Compression*:

# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(s: str) -> str:
    pass


# Tests


def test_compresses_string_with_repeated_characters():
    assert string_compression("aabcccccaaa") == "a2b1c5a3"


def test_returns_original_if_compression_does_not_reduce_length():
    assert string_compression("abcde") == "abcde"


def test_returns_empty_string_for_empty_input():
    assert string_compression("") == ""


def test_returns_single_character_for_single_character_string():
    assert string_compression("a") == "a"


def test_compresses_uppercase_and_lowercase_letters():
    assert string_compression("AAAbbbCCCddd") == "A3b3C3d3"


def test_returns_original_if_no_repeated_characters():
    assert string_compression("abcdef") == "abcdef"
