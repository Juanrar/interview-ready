# 3. *Stack of Plates*:

# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave
# identically to a single stack (that is, pop() should return the same values as it would if
# there were just a single stack).

# FOLLOW UP: Implement a function pop_at(index) which performs a pop operation on a specific sub-stack.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class StackOfPlates(Generic[T]):
    def __init__(self, capacity: int):
        pass

    def push(self, value: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass


# Tests


def test_push_and_pop():
    stack = StackOfPlates(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

    stack.push(4)
    stack.push(5)
    stack.push(6)

    assert stack.pop() == 6
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() is None


def test_push_and_pop_from_multiple_stacks():
    stack = StackOfPlates(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)  # New stack
    stack.push(4)
    stack.push(5)  # New stack

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_pop_from_empty_stack_returns_none():
    assert StackOfPlates(2).pop() is None


def test_push_beyond_capacity_creates_new_stack():
    stack = StackOfPlates(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)  # New stack
    stack.push(4)

    assert stack.pop() == 4
    assert stack.pop() == 3
