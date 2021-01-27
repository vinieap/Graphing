from graph_utils import Vertex, Edge
import argparse
from random import randrange, choice


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="d for directed and u for undirected", type=str, choices=['d','u'])
    parser.add_argument("-v ", '--vertices', help="The number of vertices in graph", type=int)
    parser.add_argument('-e', '--edges', help='Number of edges in graph', type=int)

    args = parser.parse_args()

    graph_type, vertices, edges = args.type, args.vertices, args.edges

    assert vertices > 1 and edges > 1, "Number of vertices and edges must be greater than 1"
    
    if graph_type == 'u':
        assert edges <= vertices * (vertices - 1) / 2, f"Number of edges should be equal to or less than {int(vertices * (vertices - 1) / 2)} for an undirected graph with {vertices} vertices."
    else:
        assert edges <= vertices * (vertices - 1), f"Number of edges should be equal to or less than {vertices * (vertices - 1)} for a directed graph with {vertices} vertices."

    return graph_type, vertices, edges


def createUndirectedGraph(vertices, numEdges):
    edges = []

    for x in range(numEdges):
        firstVertex = choice(vertices):


def createDirectedGraph(vertices, numEdges):
    return


def createGraph(graph_type , numVertices, numEdges):
    vertices = [Vertex(randrange(1, 1000, step=1)) for x in range(numVertices)]
    edges = createUndirectedGraph(vertices, numEdges) if graph_type == 'u' else createDirectedGraph(vertices, numEdges)
    

if __name__ == '__main__':
    graph_type, vertices, edges = parseArgs()

    print(f"[Info] Type of Graph: {'Undirected' if graph_type == 'u' else 'Directed'}")
    print(f"[Info] Number of Vertices: {vertices}")
    print(f"[Info] Number of Edges: {edges}")
