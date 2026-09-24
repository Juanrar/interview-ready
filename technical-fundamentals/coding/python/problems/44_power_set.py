# 4. *Power Set*:

# Write a method to return all subsets of a set.

# Example
# Input: [1, 2, 3]
# Output: [ [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3] ]


def power_set(values: list[int]) -> list[list[int]]:
    pass


# Tests


def normalized(subsets: list[list[int]]) -> list[list[int]]:
    """Sorts every subset and the list of subsets, so the order does not matter."""
    return sorted(sorted(subset) for subset in subsets)


def test_returns_power_set_of_3_elements():
    expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert normalized(power_set([1, 2, 3])) == normalized(expected)


def test_returns_power_set_of_empty_set():
    assert normalized(power_set([])) == [[]]


def test_returns_power_set_of_4_elements():
    expected = [
        [1],
        [1, 4],
        [1, 3, 4],
        [1, 3],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 4],
        [1, 2],
        [2],
        [2, 4],
        [2, 3, 4],
        [2, 3],
        [3],
        [3, 4],
        [4],
        [],
    ]
    assert normalized(power_set([1, 2, 3, 4])) == normalized(expected)
