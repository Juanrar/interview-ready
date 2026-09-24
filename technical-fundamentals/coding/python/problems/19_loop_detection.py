# 9. *Loop Detection*:

# Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop.

# ```
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# ```

# ```
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def detect_loop(head: Optional[Node[T]]) -> Optional[Node[T]]:
    pass


# Tests


def build_list(*values, tail=None):
    head = tail
    for value in reversed(values):
        head = Node(value, head)
    return head


def test_returns_none_if_list_has_only_one_node():
    assert detect_loop(Node(1)) is None


def test_returns_none_if_list_has_no_loop():
    assert detect_loop(build_list(1, 2, 3, 4, 5)) is None


def test_returns_node_at_the_beginning_of_the_loop():
    # 1 -> 2 -> ... -> 9 -> 31 -> 32 -> 31
    loop_node = Node(31, Node(32))
    loop_node.next.next = loop_node
    head = build_list(1, 2, 3, 4, 5, 6, 7, 8, 9, tail=loop_node)
    assert detect_loop(head) is loop_node


def test_returns_node_at_the_beginning_of_a_longer_loop():
    # 1 -> 2 -> ... -> 10 -> 11 -> 12 -> 13 -> 11
    loop_node = Node(11, Node(12, Node(13)))
    loop_node.next.next.next = loop_node
    head = build_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, tail=loop_node)
    assert detect_loop(head) is loop_node
