# 2. *Minimal Tree*:

# Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.
#
# A binary search tree is a search where for each node,
# lesser elements are on the left node, and greater elements on the right node.
#
# Input: [1,2,3,4,5,6,7,8]
# Output:
#      5
#   2  |  7
# 1   3|6   8

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


def minimal_tree(sorted_array: list[T]) -> Optional[TreeNode[T]]:
    pass


# Tests


def test_creates_minimal_bst_from_3_elements():
    expected = TreeNode(2, TreeNode(1), TreeNode(3))
    assert minimal_tree([1, 2, 3]) == expected


def test_creates_minimal_bst_from_5_elements():
    expected = TreeNode(
        3,
        TreeNode(2, left=TreeNode(1)),
        TreeNode(5, left=TreeNode(4)),
    )
    assert minimal_tree([1, 2, 3, 4, 5]) == expected


def test_creates_minimal_bst_from_7_elements():
    expected = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7)),
    )
    assert minimal_tree([1, 2, 3, 4, 5, 6, 7]) == expected


def test_returns_none_for_empty_array():
    assert minimal_tree([]) is None
