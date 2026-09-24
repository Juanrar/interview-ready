# Write the basic tree algorithms of Depth-first-search and Breadth-first search.

from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    value: T
    left: Optional["TreeNode[T]"] = None
    right: Optional["TreeNode[T]"] = None


class Tree(Generic[T]):
    def bfs(
        self, node: Optional[TreeNode[T]], visit: Callable[[TreeNode[T]], None]
    ) -> None:
        pass

    def dfs(
        self, node: Optional[TreeNode[T]], visit: Callable[[TreeNode[T]], None]
    ) -> None:
        pass


# Tests


def test_dfs_navigates_the_tree_in_order():
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(5, TreeNode(6, TreeNode(7)), TreeNode(8)),
    )
    order = []
    Tree().dfs(root, lambda node: order.append(node.value))
    assert order == [1, 2, 3, 4, 5, 6, 7, 8]


def test_bfs_navigates_the_tree_in_order():
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6, TreeNode(8)), TreeNode(7)),
    )
    order = []
    Tree().bfs(root, lambda node: order.append(node.value))
    assert order == [1, 2, 3, 4, 5, 6, 7, 8]
