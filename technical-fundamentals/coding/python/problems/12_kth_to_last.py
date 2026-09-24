# 2.  *Return Kth to Last*:

# Implement an algorithm to find the kth to last element of a singly linked list.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def kth_to_last(head: Node[T], k: int) -> Optional[Node[T]]:
    pass


# Tests


def build_list(*values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def test_returns_none_if_k_is_less_than_1():
    assert kth_to_last(Node(1), 0) is None


def test_returns_none_if_k_is_greater_than_length():
    assert kth_to_last(Node(1), 2) is None


def test_returns_kth_to_last_when_k_is_valid():
    head = build_list(1, 2, 3, 4, 5)
    node4 = head.next.next.next
    # The 2nd to last element in this list is 4
    assert kth_to_last(head, 2) is node4


def test_returns_head_if_k_equals_length():
    head = build_list(1, 2, 3, 4, 5)
    assert kth_to_last(head, 5) is head
