# 3.  URLify:

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.


def urlify(s: str) -> str:
    result = ""
    for i in range(len(s)):
        if s[i] == " ":
            result += "%20"
        else:
            result += s[i]
    return result


# Tests


def test_replaces_spaces_with_percent_20():
    assert urlify("ab c") == "ab%20c"


def test_handles_leading_and_trailing_spaces():
    assert urlify("  ab c  ") == "%20%20ab%20c%20%20"


def test_returns_empty_string_when_input_is_empty():
    assert urlify("") == ""


def test_does_not_modify_string_without_spaces():
    assert urlify("abc") == "abc"


def test_handles_multiple_consecutive_spaces():
    assert urlify("a  b   c") == "a%20%20b%20%20%20c"


def test_handles_special_characters():
    assert urlify("a b!c") == "a%20b!c"


def test_mr_john_smith():
    assert urlify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"
