from typing import Union

from edge import Edge
from node import Node

from itertools import combinations 

class Undirected_Graph:
    def __init__(self):

        self.nodes = set()
        self.edges = set()
        self.neighbors = dict()
        

    def add_node(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("node must be a Node object")

        if node not in self.nodes:
            self.nodes.add(node)
            self.neighbors[node] = set()        

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
            self.add_node(node1)

        if node2 not in self.nodes:
            self.add_node(node2)

        edge = Edge(node1, node2, weight)

        if edge not in self.edges:
            self.edges.add(edge)

            self.neighbors[node1].add(node2)
            self.neighbors[node2].add(node1)

    def add_edges(self, edges: list):
        if not isinstance(edges, list):
            raise TypeError("edges must be a list")

        for edge in edges:
            self.add_edge(*edge)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    
    def get_neighbors(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("node must be a Node object")

        if node not in self.nodes:
            raise ValueError("node not in graph")

        return self.neighbors.get(node, set())

    def degree(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("node must be a Node object")

        if node not in self.nodes:
            return -1
        
        return len(self.get_neighbors(node))

    def is_connected(self):
        if len(self.nodes) == 0 or len(self.nodes) == 1:
            return True

        seen = set()
        queue = [next(iter(self.nodes))] # Cannot subscript sets

        while len(queue) != 0:
            node = queue.pop(0)
            seen.add(node)

            neighbors = self.get_neighbors(node)

            for neighbor in neighbors:
                if neighbor not in seen:
                    queue.append(neighbor)

        return len(seen) == len(self.nodes)

    def is_complete(self):
        if len(self.nodes) == 0 or len(self.nodes) == 1:
            return True

        for n1, n2 in combinations(self.nodes, 2):
            if n1 not in self.neighbors[n2]:
                return False

        return True

    @staticmethod
    def from_edges(edges):
        g = Undirected_Graph()

        return g.add_edges(edges)

    @staticmethod
    def from_nodes(nodes):
        g = Undirected_Graph()

        return g.add_nodes(nodes)

