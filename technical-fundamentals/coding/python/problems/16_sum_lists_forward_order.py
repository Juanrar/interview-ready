# 6.  Suppose the digits are stored in forward order. Repeat the above problem.

# ```
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
# Output: 9 -> 1 -> 2. That is, 912.
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def sum_lists_forward_order(
    list1: Optional[Node[int]], list2: Optional[Node[int]]
) -> Optional[Node[int]]:
    pass


# Tests


def test_sums_one_element_each_without_carryover():
    assert sum_lists_forward_order(Node(1), Node(2)) == Node(3)


def test_sums_two_elements_each_without_carryover():
    list1 = Node(1, Node(3))
    list2 = Node(2, Node(3))
    assert sum_lists_forward_order(list1, list2) == Node(3, Node(6))


def test_sums_without_carryover():
    # 123 + 456 = 579
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(4, Node(5, Node(6)))
    assert sum_lists_forward_order(list1, list2) == Node(5, Node(7, Node(9)))


def test_sums_with_carryover():
    # 999 + 1 = 1000
    list1 = Node(9, Node(9, Node(9)))
    list2 = Node(1)
    expected = Node(1, Node(0, Node(0, Node(0))))
    assert sum_lists_forward_order(list1, list2) == expected


def test_sums_lists_with_different_lengths():
    # 1234 + 56 = 1290
    list1 = Node(1, Node(2, Node(3, Node(4))))
    list2 = Node(5, Node(6))
    expected = Node(1, Node(2, Node(9, Node(0))))
    assert sum_lists_forward_order(list1, list2) == expected


def test_sums_two_empty_lists():
    assert sum_lists_forward_order(None, None) is None


def test_sums_one_empty_list_and_one_non_empty_list():
    # 123 + 0 = 123
    list1 = Node(1, Node(2, Node(3)))
    assert sum_lists_forward_order(list1, None) == Node(1, Node(2, Node(3)))
