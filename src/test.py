from edge import Edge
from graphs import Undirected_Graph
from node import Node

g = Undirected_Graph()

n1 = Node(1, "n1")
n2 = Node(2, "n2")
n3 = Node(3, "n3")

g.add_nodes([n1, n2, n3])

edges = [
    (n1, n2, 1),
    (n1, n3, 2),
]

g.add_edges(edges)

for node in g.get_nodes():
    print(node)

for edge in g.get_edges():
    print(edge)

g2 = Undirected_Graph.from_edges(edges)

for node in g.get_nodes():
    print(node)

for edge in g.get_edges():
    print(edge)
