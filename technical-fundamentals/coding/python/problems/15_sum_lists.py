# 5. *Sum Lists*: You have two numbers represented by a linked list,
# where each node contains a single digit. The digits are stored in reverse order,
# such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.

# ```
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def sum_lists(
    list1: Optional[Node[int]], list2: Optional[Node[int]]
) -> Optional[Node[int]]:
    pass


# Tests


def test_sums_without_carryover():
    # 321 + 654 = 975
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(4, Node(5, Node(6)))
    assert sum_lists(list1, list2) == Node(5, Node(7, Node(9)))


def test_sums_with_carryover():
    # 999 + 1 = 1000
    list1 = Node(9, Node(9, Node(9)))
    list2 = Node(1)
    assert sum_lists(list1, list2) == Node(0, Node(0, Node(0, Node(1))))


def test_sums_lists_with_different_lengths():
    # 4321 + 65 = 4386
    list1 = Node(1, Node(2, Node(3, Node(4))))
    list2 = Node(5, Node(6))
    assert sum_lists(list1, list2) == Node(6, Node(8, Node(3, Node(4))))
