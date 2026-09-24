# 5. *Recursive Multiply*:

# Write a recursive function to multiply two positive integers without using the * operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.


def recursive_multiply(a: int, b: int) -> int:
    pass


# Tests


def test_returns_product_of_two_positive_integers():
    assert recursive_multiply(3, 4) == 12
    assert recursive_multiply(5, 7) == 35
    assert recursive_multiply(9, 2) == 18


def test_returns_0_when_one_number_is_0():
    assert recursive_multiply(0, 10) == 0
    assert recursive_multiply(8, 0) == 0
