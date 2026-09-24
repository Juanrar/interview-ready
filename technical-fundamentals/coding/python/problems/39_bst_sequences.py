# 9. *BST Sequences*: A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

# ```
# EXAMPLE Input:
#             2
#            / \
#           1   3
# Output: [[2, 1, 3], [2, 3, 1]]
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


def bst_sequences(root: TreeNode[T]) -> list[list[T]]:
    pass


# Tests


def test_returns_sequences_for_3_nodes():
    #      2
    #     / \
    #    1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    sequences = bst_sequences(root)
    assert [2, 1, 3] in sequences
    assert [2, 3, 1] in sequences


def test_returns_sequences_for_7_nodes():
    #         5
    #        / \
    #       3   7
    #      / \ / \
    #     2  4 6  8
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2), TreeNode(4)),
        TreeNode(7, TreeNode(6), TreeNode(8)),
    )
    sequences = bst_sequences(root)
    assert len(sequences) == 80
    for expected in [
        [5, 3, 7, 2, 4, 6, 8],
        [5, 3, 7, 2, 6, 4, 8],
        [5, 3, 7, 4, 2, 6, 8],
        [5, 3, 7, 4, 6, 2, 8],
        [5, 7, 3, 2, 4, 6, 8],
        [5, 7, 3, 2, 6, 4, 8],
        [5, 7, 3, 4, 2, 6, 8],
        [5, 7, 3, 4, 6, 2, 8],
    ]:
        assert expected in sequences
