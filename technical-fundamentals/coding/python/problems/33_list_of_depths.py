# 3. *List of Depths*:

# Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth (e.g., if you have a tree with depth D,
# you'll have D linked lists).

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


@dataclass
class ListNode(Generic[T]):
    value: T
    next: Optional["ListNode[T]"] = None


def list_of_depths(root: Optional[TreeNode[T]]) -> list[ListNode[T]]:
    pass


# Tests


def test_creates_linked_lists_of_nodes_at_each_depth():
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    #    /
    #   7
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
        TreeNode(3, right=TreeNode(6)),
    )
    expected = [
        ListNode(1),  # Depth 0
        ListNode(2, ListNode(3)),  # Depth 1
        ListNode(4, ListNode(5, ListNode(6))),  # Depth 2
        ListNode(7),  # Depth 3
    ]
    assert list_of_depths(root) == expected


def test_creates_linked_list_for_single_node_tree():
    assert list_of_depths(TreeNode(1)) == [ListNode(1)]
