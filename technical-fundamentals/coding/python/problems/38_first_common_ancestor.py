# 8. *First Common Ancestor*:

# Design an algorithm and write code to find the first common ancestor of two nodes
# in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


def first_common_ancestor(
    root: Optional[TreeNode[T]], p: TreeNode[T], q: TreeNode[T]
) -> Optional[TreeNode[T]]:
    pass


# Tests


def test_returns_first_common_ancestor():
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    # Common ancestor of 2 and 3 is 1
    assert first_common_ancestor(root, root.left, root.right) is root
    # Common ancestor of 4 and 5 is 2
    assert first_common_ancestor(root, root.left.left, root.left.right) is root.left
    # Common ancestor of 4 and 7 is 1
    assert first_common_ancestor(root, root.left.left, root.right.right) is root
