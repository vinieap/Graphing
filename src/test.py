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

print(f"Nodes:")

for node in g.get_nodes():
    print(node)

print(f"Edges:")

for edge in g.get_edges():
    print(edge)

print(f"Degrees:")

for node in g.get_nodes():
    print(f"{node} Degree: {g.degree(node)}")


# Test Connectivity
print(f"G is connected? {g.is_connected()}")
print(f"G is complete? {g.is_complete()}")

print(f"Adding edge n2-n3")
g.add_edge(n2, n3, 3)

print(f"G is connnected? {g.is_connected()}")
print(f"G is complete? {g.is_complete()}")

print(f"Adding isolated node n4")
g.add_node(Node(4, "n4"))

print(f"G is connected? {g.is_connected()}")
print(f"G is complete? {g.is_complete()}")
