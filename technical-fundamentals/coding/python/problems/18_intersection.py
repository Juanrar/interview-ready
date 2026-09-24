# 8.  *Intersection*:

# Given two (singly) linked lists, determine if the two lists intersect.
# Return the first intersecting node. Note that the intersection is defined
# based on reference, not value.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def intersection(
    list1: Optional[Node[T]], list2: Optional[Node[T]]
) -> Optional[Node[T]]:
    pass


# Tests


def test_returns_none_if_lists_do_not_intersect():
    # List 1: 1 -> 2 -> 3 -> 4
    # List 2: 5 -> 6 -> 7 -> 8
    list1 = Node(1, Node(2, Node(3, Node(4))))
    list2 = Node(5, Node(6, Node(7, Node(8))))
    assert intersection(list1, list2) is None


def test_returns_none_if_lists_only_share_values():
    # Same values, different nodes: they do not intersect.
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(1, Node(2, Node(3)))
    assert intersection(list1, list2) is None


def test_returns_intersection_node():
    # Common part: 7 -> 8 -> 9
    # List 1: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
    # List 2: 5 -> 6 -> 7 -> 8 -> 9
    common = Node(7, Node(8, Node(9)))
    list1 = Node(1, Node(2, Node(3, Node(4, common))))
    list2 = Node(5, Node(6, common))
    assert intersection(list1, list2) is common


def test_returns_intersection_at_the_head():
    common = Node(1, Node(2, Node(3)))
    assert intersection(common, common) is common


def test_returns_intersection_when_one_list_contains_the_other():
    # List 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    # List 2: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    list1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    list2 = Node(0, list1)
    assert intersection(list1, list2) is list1
