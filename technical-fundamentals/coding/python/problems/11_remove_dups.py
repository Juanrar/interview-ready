# 1. *Remove Dups*:

# Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
#
# 1 -> 2 -> 2-> 2 -> 4

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def remove_dups(head: Optional[Node[T]] = None) -> Optional[Node[T]]:
    pass


# Tests


def test_removes_duplicates():
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("b")
    node1.next = node2
    node2.next = node3

    expected = Node("a", Node("b"))
    assert remove_dups(node1) == expected


def test_no_duplicates():
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node1.next = node2
    node2.next = node3

    expected = Node("a", Node("b", Node("c")))
    assert remove_dups(node1) == expected


def test_multiple_duplicates():
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("a")
    node1.next = node2
    node2.next = node3

    assert remove_dups(node1) == Node("a")


def test_empty_list():
    assert remove_dups() is None


def test_list_with_one_node():
    node1 = Node("a")
    assert remove_dups(node1) == node1
