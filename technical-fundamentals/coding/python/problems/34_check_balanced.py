# 4. *Check Balanced*:

# Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more than one.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


def check_balanced(tree: Optional[TreeNode[T]] = None) -> bool:
    pass


# Tests


def test_returns_true_for_balanced_tree():
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    assert check_balanced(root) is True


def test_returns_false_for_unbalanced_tree():
    #        1
    #       /
    #      2
    #     /
    #    3
    #   /
    #  4
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert check_balanced(root) is False


def test_returns_true_for_empty_tree():
    assert check_balanced(None) is True
