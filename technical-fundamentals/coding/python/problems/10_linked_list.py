# 10. *Implement a Linked List*:

# Create the data structure with the corresponding initial functions:

from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


class LinkedList(Generic[T]):
    def __init__(self, head: Optional[Node[T]] = None):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.length: int = 0

    def push(self, value: T) -> None:
        """Adds a node with value at the end of the list."""
        pass

    def filter(self, predicate: Callable[[T], bool]) -> "LinkedList[T]":
        """Returns a new list with the values for which predicate returns True."""
        pass

    def visit(self, fn: Callable[[Node[T]], None]) -> None:
        """Calls fn with every node, from head to tail."""
        pass

    def remove(self, value: T) -> Optional[Node[T]]:
        """Removes the first node with value. Returns the removed node or None."""
        pass

    def merge(self, other: "LinkedList[T]") -> None:
        """Appends the nodes of other at the end of this list."""
        pass

    def print(self) -> None:
        """Prints the list as "1 -> 2 -> 3"."""
        pass

    # extra

    # def find(self, predicate) -> Optional[Node[T]]: ...
    # def get(self, index: int) -> Optional[Node[T]]: ...
    # def __iter__(self): ...


# Tests


def values(linked_list: LinkedList) -> list:
    result = []
    node = linked_list.head
    while node:
        result.append(node.value)
        node = node.next
    return result


def test_empty_list():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_constructor_with_head():
    linked_list = LinkedList(Node(1))
    assert values(linked_list) == [1]
    assert linked_list.tail.value == 1
    assert linked_list.length == 1


def test_push_adds_values_at_the_end():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert values(linked_list) == [1, 2, 3]
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3
    assert linked_list.length == 3


def test_filter_returns_new_list():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4]:
        linked_list.push(value)
    evens = linked_list.filter(lambda value: value % 2 == 0)
    assert values(evens) == [2, 4]
    assert values(linked_list) == [1, 2, 3, 4]


def test_visit_calls_fn_for_every_node_in_order():
    linked_list = LinkedList()
    for value in [1, 2, 3]:
        linked_list.push(value)
    visited = []
    linked_list.visit(lambda node: visited.append(node.value))
    assert visited == [1, 2, 3]


def test_remove_head_middle_and_tail():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4]:
        linked_list.push(value)

    assert linked_list.remove(2).value == 2
    assert values(linked_list) == [1, 3, 4]

    linked_list.remove(1)
    assert values(linked_list) == [3, 4]
    assert linked_list.head.value == 3

    linked_list.remove(4)
    assert values(linked_list) == [3]
    assert linked_list.tail.value == 3
    assert linked_list.length == 1


def test_remove_missing_value_returns_none():
    linked_list = LinkedList()
    linked_list.push(1)
    assert linked_list.remove(5) is None
    assert values(linked_list) == [1]


def test_merge_appends_other_list():
    first = LinkedList()
    first.push(1)
    first.push(2)
    second = LinkedList()
    second.push(3)
    second.push(4)

    first.merge(second)
    assert values(first) == [1, 2, 3, 4]
    assert first.tail.value == 4
    assert first.length == 4


def test_print(capsys):
    linked_list = LinkedList()
    for value in [1, 2, 3]:
        linked_list.push(value)
    linked_list.print()
    assert capsys.readouterr().out.strip() == "1 -> 2 -> 3"
