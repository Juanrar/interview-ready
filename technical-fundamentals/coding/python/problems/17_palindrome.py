# 7. *Palindrome*:

# Implement a function to check if a linked list is a palindrome.

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


def is_palindrome(head: Optional[Node[T]]) -> bool:
    pass


# Tests


def build_list(*values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def test_single_node_list_is_palindrome():
    assert is_palindrome(Node(1)) is True


def test_palindrome_with_odd_number_of_nodes():
    assert is_palindrome(build_list(1, 2, 3, 2, 1)) is True


def test_non_palindrome_list():
    assert is_palindrome(build_list(1, 2, 3, 4, 5)) is False


def test_palindrome_with_even_number_of_nodes():
    assert is_palindrome(build_list(1, 2, 2, 1)) is True
