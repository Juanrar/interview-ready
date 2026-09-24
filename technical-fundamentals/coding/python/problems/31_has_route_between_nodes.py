# 1. *Route Between Nodes*:

# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.

from dataclasses import dataclass, field


# eq=False: nodes are compared by identity, because graphs can have cycles.
@dataclass(eq=False)
class GraphNode:
    value: int
    neighbors: list["GraphNode"] = field(default_factory=list)


def has_route_between_nodes(start: GraphNode, end: GraphNode) -> bool:
    pass


# Tests


def test_has_route_between_connected_nodes():
    #   Graph:
    #   1 -> 2 -> 3 -> 4
    #   |         |
    #   5         6
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node6 = GraphNode(6)

    node1.neighbors = [node2, node5]
    node2.neighbors = [node3]
    node3.neighbors = [node4, node6]
    node6.neighbors = [node3]  # Back edge, creates a cycle

    assert has_route_between_nodes(node1, node4) is True
    assert has_route_between_nodes(node4, node1) is False  # No reverse route
    assert has_route_between_nodes(node2, node5) is False
    assert has_route_between_nodes(node1, node6) is True  # Route via node 3


def test_no_route_between_disconnected_nodes():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)

    assert has_route_between_nodes(node1, node2) is False
    assert has_route_between_nodes(node2, node3) is False
    assert has_route_between_nodes(node1, node3) is False


def test_no_route_between_nodes_without_neighbors():
    assert has_route_between_nodes(GraphNode(1), GraphNode(2)) is False
