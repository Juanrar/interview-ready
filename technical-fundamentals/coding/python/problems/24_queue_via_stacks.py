# 4. *Queue via Stacks*:

# Implement a MyQueue class which implements a queue using two stacks.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class MyQueue(Generic[T]):
    def __init__(self):
        pass

    def enqueue(self, value: T) -> None:
        pass

    def dequeue(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass


# Tests


def test_enqueue_and_dequeue():
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() is None


def test_enqueue_and_dequeue_mixed_with_peek():
    queue = MyQueue()

    queue.enqueue(1)
    assert queue.peek() == 1
    queue.enqueue(2)
    assert queue.peek() == 1

    assert queue.dequeue() == 1
    assert queue.peek() == 2

    queue.enqueue(3)
    assert queue.peek() == 2

    assert queue.dequeue() == 2
    assert queue.peek() == 3

    assert queue.dequeue() == 3
    assert queue.peek() is None


def test_peek_from_empty_queue_returns_none():
    assert MyQueue().peek() is None


def test_is_empty_returns_true_for_empty_queue():
    assert MyQueue().is_empty() is True


def test_is_empty_returns_false_for_non_empty_queue():
    queue = MyQueue()
    queue.enqueue(1)
    assert queue.is_empty() is False
