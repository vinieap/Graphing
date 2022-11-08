from typing import Union

from edge import Edge
from node import Node


class Undirected_Graph:
    def __init__(self, nodes: list = None):

        self.nodes = set()
        self.edges = set()

        if nodes:
            self.nodes = nodes

    def add_node(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("node must be a Node object")

        if node not in self.nodes:
            self.nodes.add(node)

    def add_nodes(self, nodes: list):
        if not isinstance(nodes, list):
            raise TypeError("nodes must be a list")

        for node in nodes:
            self.add_node(node)

    def add_edge(self, node1: Node, node2: Node, weight: Union[int, float] = 0):
        if not isinstance(node1, Node) or not isinstance(node2, Node):
            raise TypeError("nodes must be Node objects")

        if not isinstance(weight, int) and not isinstance(weight, float):
            raise TypeError("weight must be an integer or float")

        if node1 not in self.nodes:
            self.nodes.add(node1)

        if node2 not in self.nodes:
            self.nodes.add(node2)

        edge = Edge(node1, node2, weight)

        if edge not in self.edges:
            self.edges.add(edge)

    def add_edges(self, edges: list):
        if not isinstance(edges, list):
            raise TypeError("edges must be a list")

        for edge in edges:
            self.add_edge(*edge)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    @staticmethod
    def from_edges(edges):
        g = Undirected_Graph()

        return g.add_edges(edges)

    @staticmethod
    def from_nodes(nodes):
        g = Undirected_Graph()

        return g.add_nodes(nodes)

