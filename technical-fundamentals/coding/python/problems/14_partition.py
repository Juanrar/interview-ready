# 4. *Partition*:

# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

# ```
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# ```

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def partition(head: Optional[Node[T]], x: T) -> Optional[Node[T]]:
    pass


# Tests


def build_list(*values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def values(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def test_partitions_the_list():
    result = values(partition(build_list(3, 5, 8, 5, 10, 2, 1), 5))
    # Expected something like: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
    assert len(result) == 7
    assert all(value < 5 for value in result[:3])
    assert all(value >= 5 for value in result[3:])


def test_single_node_list():
    result = partition(Node(5), 5)
    assert result.value == 5
    assert result.next is None


def test_all_nodes_less_than_x():
    result = values(partition(build_list(3, 2, 1, 4, 5), 6))
    assert len(result) == 5
    assert all(value < 6 for value in result)


def test_all_nodes_greater_than_or_equal_to_x():
    result = values(partition(build_list(3, 2, 1, 4, 5), 0))
    assert len(result) == 5
    assert all(value >= 0 for value in result)
