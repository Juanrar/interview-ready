# 5. *Sort Stack*:

# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and is_empty.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class SortStack(Generic[T]):
    def __init__(self):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass


# Tests


def test_push_keeps_smallest_on_top():
    stack = SortStack()

    stack.push(3)
    assert stack.peek() == 3
    stack.push(1)
    assert stack.peek() == 1
    stack.push(5)
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 1
    stack.push(4)
    assert stack.peek() == 1


def test_pop_returns_elements_in_sorted_order():
    stack = SortStack()
    for value in [3, 1, 5, 2, 4]:
        stack.push(value)

    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() == 4
    assert stack.pop() == 5
    assert stack.pop() is None


def test_peek_does_not_remove_the_top():
    stack = SortStack()
    stack.push(3)
    stack.push(1)
    stack.push(5)

    assert stack.peek() == 1
    assert stack.peek() == 1


def test_is_empty_returns_true_for_empty_stack():
    assert SortStack().is_empty() is True


def test_is_empty_returns_false_for_non_empty_stack():
    stack = SortStack()
    stack.push(1)
    assert stack.is_empty() is False
