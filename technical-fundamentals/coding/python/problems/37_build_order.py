# 7. *Build Order*:

# You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is
# dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow
# the projects to be built. If there is no valid build order, raise an error
# with the message "No valid build order exists".
#
# The tests expect one specific order: build in rounds, and in each round take every
# project whose dependencies are already built, in the order they appear in projects.

# ```
# EXAMPLE Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: e, f, a, b, d, c
# ```

import pytest


def build_order(projects: list[str], dependencies: list[list[str]]) -> list[str]:
    pass


# Tests


def test_returns_build_order_for_valid_input():
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [
        ["a", "d"],
        ["f", "b"],
        ["b", "d"],
        ["f", "a"],
        ["d", "c"],
    ]
    assert build_order(projects, dependencies) == ["e", "f", "a", "b", "d", "c"]


def test_raises_error_when_no_valid_order_exists():
    # "f" is a dependency but not a project.
    projects = ["a", "b", "c", "d", "e"]
    dependencies = [
        ["a", "d"],
        ["f", "b"],
        ["b", "d"],
        ["f", "a"],
        ["d", "c"],
    ]
    with pytest.raises(Exception, match="No valid build order exists"):
        build_order(projects, dependencies)


def test_raises_error_for_cyclic_dependencies():
    projects = ["a", "b"]
    dependencies = [["a", "b"], ["b", "a"]]
    with pytest.raises(Exception, match="No valid build order exists"):
        build_order(projects, dependencies)


def test_returns_build_order_for_single_project():
    assert build_order(["a"], []) == ["a"]


def test_returns_empty_build_order_for_empty_input():
    assert build_order([], []) == []
