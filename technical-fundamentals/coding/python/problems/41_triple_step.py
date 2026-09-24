# 1. *Triple Step*:

# A child is running up a staircase with n steps and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count
# how many possible ways the child can run up the stairs.


def triple_step(n: int) -> int:
    pass


# Tests


def test_returns_count_for_valid_input():
    assert triple_step(0) == 0  # No steps
    assert triple_step(1) == 1  # (1)
    assert triple_step(2) == 2  # (1, 1), (2)
    assert triple_step(3) == 4  # (1, 1, 1), (1, 2), (2, 1), (3)
    assert triple_step(4) == 7
    assert triple_step(5) == 13


def test_returns_0_for_negative_input():
    assert triple_step(-1) == 0
    assert triple_step(-10) == 0
