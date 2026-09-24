# 6. *Successor*:

# Write an algorithm to find the "next" node
# (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None
    # Link to parent node. Excluded from == and repr to avoid infinite recursion.
    parent: Optional["TreeNode[T]"] = field(default=None, compare=False, repr=False)


def successor(node: TreeNode[T]) -> Optional[TreeNode[T]]:
    pass


# Tests


def test_returns_in_order_successor():
    #         5
    #        / \
    #       3   7
    #      / \ / \
    #     2  4 6  8
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node8 = TreeNode(8)
    node3 = TreeNode(3, node2, node4)
    node7 = TreeNode(7, node6, node8)
    node5 = TreeNode(5, node3, node7)

    node2.parent = node3
    node4.parent = node3
    node3.parent = node5
    node6.parent = node7
    node8.parent = node7
    node7.parent = node5

    assert successor(node2).value == 3
    assert successor(node3).value == 4
    assert successor(node4).value == 5
    assert successor(node5).value == 6
    assert successor(node6).value == 7
    assert successor(node7).value == 8
    assert successor(node8) is None


def test_returns_none_for_node_without_successor():
    assert successor(TreeNode(1)) is None
