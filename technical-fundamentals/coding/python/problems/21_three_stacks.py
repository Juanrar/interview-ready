# 1. *Three in One*: Describe how you could use a single array to implement three stacks.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ThreeStacks(Generic[T]):
    def __init__(self, array_length: int):
        self.array: list[Optional[T]] = []

    def push(self, stack_num: int, value: T) -> None:
        pass

    def pop(self, stack_num: int) -> Optional[T]:
        pass

    def peek(self, stack_num: int) -> Optional[T]:
        pass


# Tests


def test_push_and_pop_from_stack_1():
    stacks = ThreeStacks(9)
    stacks.push(0, 1)
    stacks.push(0, 2)
    stacks.push(0, 3)
    assert stacks.pop(0) == 3
    assert stacks.pop(0) == 2
    assert stacks.pop(0) == 1
    assert stacks.pop(0) is None


def test_push_and_pop_from_stack_2():
    stacks = ThreeStacks(9)
    stacks.push(1, 4)
    stacks.push(1, 5)
    stacks.push(1, 6)
    assert stacks.pop(1) == 6
    assert stacks.pop(1) == 5
    assert stacks.pop(1) == 4
    assert stacks.pop(1) is None


def test_push_and_pop_from_stack_3():
    stacks = ThreeStacks(9)
    stacks.push(2, 7)
    stacks.push(2, 8)
    stacks.push(2, 9)
    assert stacks.pop(2) == 9
    assert stacks.pop(2) == 8
    assert stacks.pop(2) == 7
    assert stacks.pop(2) is None


def test_stacks_do_not_mix_values():
    stacks = ThreeStacks(9)
    stacks.push(0, 1)
    stacks.push(1, 2)
    stacks.push(2, 3)
    stacks.push(0, 4)
    assert stacks.pop(2) == 3
    assert stacks.pop(1) == 2
    assert stacks.pop(0) == 4
    assert stacks.pop(0) == 1


def test_pop_from_empty_stacks():
    stacks = ThreeStacks(3)
    assert stacks.pop(0) is None
    assert stacks.pop(1) is None
    assert stacks.pop(2) is None


def test_peek_from_stacks():
    stacks = ThreeStacks(3)
    stacks.push(0, 1)
    stacks.push(1, 2)
    stacks.push(2, 3)
    assert stacks.peek(0) == 1
    assert stacks.peek(1) == 2
    assert stacks.peek(2) == 3


def test_peek_from_empty_stacks():
    stacks = ThreeStacks(3)
    assert stacks.peek(0) is None
    assert stacks.peek(1) is None
    assert stacks.peek(2) is None
