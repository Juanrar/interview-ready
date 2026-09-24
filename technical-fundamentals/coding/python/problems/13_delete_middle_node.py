# 3. *Delete Middle Node*:

# Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.

# ```
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def delete_middle_node(head: Node[T], position: int) -> Optional[Node[T]]:
    pass


# Tests


def values(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def test_deletes_middle_node_at_position_1():
    head = Node(0, Node(1, Node(2, Node(3))))
    assert delete_middle_node(head, 1) == Node(0, Node(2, Node(3)))


def test_no_deletion_if_position_is_out_of_range():
    head = Node(1, Node(2, Node(3)))
    assert values(delete_middle_node(head, 4)) == [1, 2, 3]


def test_no_deletion_if_position_is_less_than_1():
    head = Node(1, Node(2, Node(3)))
    assert values(delete_middle_node(head, 0)) == [1, 2, 3]


def test_no_deletion_if_list_has_only_one_node():
    result = delete_middle_node(Node(1), 2)
    assert result.value == 1
    assert result.next is None


def test_no_deletion_if_list_has_only_two_nodes():
    result = delete_middle_node(Node(1, Node(2)), 2)
    assert result.value == 1
    assert result.next.value == 2
    assert result.next.next is None
