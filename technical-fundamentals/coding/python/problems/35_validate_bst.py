# 5. *Validate BST*:

# Implement a function to check if a binary tree is a binary search tree.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


def validate_bst(node: Optional[TreeNode[T]]) -> bool:
    pass


# Tests


def test_returns_true_for_valid_bst():
    #      2
    #     / \
    #    1   3
    assert validate_bst(TreeNode(2, TreeNode(1), TreeNode(3))) is True


def test_returns_false_for_invalid_bst():
    #      1
    #     / \
    #    2   3
    assert validate_bst(TreeNode(1, TreeNode(2), TreeNode(3))) is False


def test_returns_false_for_invalid_bst_2():
    #      3
    #     / \
    #    2   5
    #   / \
    #  1   4
    root = TreeNode(3, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(5))
    assert validate_bst(root) is False


def test_returns_true_for_empty_tree():
    assert validate_bst(None) is True


def test_returns_true_for_single_node_tree():
    assert validate_bst(TreeNode(5)) is True
