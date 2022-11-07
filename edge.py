from typing import Union

from node import Node


class Edge:
    def __init__(self, node1: Node, node2: Node, weight: Union[int, float] = 0):

        if not isinstance(node1, Node) or not isinstance(node2, Node):
            raise TypeError("nodes must be Node objects")

        if not isinstance(weight, int) and not isinstance(weight, float):
            raise TypeError("weight must be an integer or float")

        self.nodes = (node1, node2)
        self.weight = weight

    def __str__(self):
        return f"Edge: ({self.nodes[0]}, {self.nodes[1]}) - {self.weight}"
