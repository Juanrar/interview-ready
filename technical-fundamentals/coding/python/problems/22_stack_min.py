# 2. *Stack Min*: How would you design a stack which,
# in addition to push and pop,
# has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class StackMin(Generic[T]):
    def __init__(self):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def min(self) -> Optional[T]:
        pass


# Tests


def test_push_and_pop():
    stack = StackMin()
    stack.push(5)
    stack.push(2)
    stack.push(8)
    stack.push(1)

    assert stack.min() == 1
    assert stack.pop() == 1
    assert stack.min() == 2
    assert stack.pop() == 8
    assert stack.min() == 2
    assert stack.pop() == 2
    assert stack.min() == 5
    assert stack.pop() == 5
    assert stack.min() is None


def test_min_returns_none_when_stack_is_empty():
    assert StackMin().min() is None


def test_push_and_pop_mixed_with_min():
    stack = StackMin()

    stack.push(3)
    assert stack.min() == 3
    stack.push(5)
    assert stack.min() == 3
    stack.push(2)
    assert stack.min() == 2
    stack.push(1)
    assert stack.min() == 1

    assert stack.pop() == 1
    assert stack.min() == 2
    assert stack.pop() == 2
    assert stack.min() == 3

    stack.push(0)
    assert stack.min() == 0
    assert stack.pop() == 0
    assert stack.min() == 3

    assert stack.pop() == 5
    assert stack.min() == 3
    assert stack.pop() == 3
    assert stack.min() is None
