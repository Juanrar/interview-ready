# 6. *Animal Shelter*:

# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat
# (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations
# such as enqueue, dequeue_any, dequeue_dog, and dequeue_cat.
# You may use the built-in collections.deque data structure.

from typing import Literal, Optional

AnimalType = Literal["dog", "cat"]


class Animal:
    def __init__(self, type: AnimalType):
        self.type = type


class AnimalShelter:
    def __init__(self):
        pass

    def enqueue(self, type: AnimalType) -> None:
        pass

    def dequeue_any(self) -> Optional[Animal]:
        pass

    def dequeue_dog(self) -> Optional[Animal]:
        pass

    def dequeue_cat(self) -> Optional[Animal]:
        pass


# Tests


def test_enqueue_and_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")

    assert shelter.dequeue_any().type == "dog"  # Oldest animal is a dog
    assert shelter.dequeue_any().type == "cat"  # Oldest animal is a cat

    shelter.enqueue("cat")
    shelter.enqueue("dog")

    assert shelter.dequeue_dog().type == "dog"

    shelter.enqueue("dog")

    assert shelter.dequeue_cat().type == "cat"


def test_dequeue_dog_skips_older_cats():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")

    assert shelter.dequeue_dog().type == "dog"
    assert shelter.dequeue_any().type == "cat"
    assert shelter.dequeue_any() is None


def test_dequeue_methods_return_none_when_shelter_is_empty():
    shelter = AnimalShelter()
    assert shelter.dequeue_any() is None
    assert shelter.dequeue_dog() is None
    assert shelter.dequeue_cat() is None
