class Vertex:

    def __init__(self, weight):
        self.weight = weight
        # All edges "coming out" of vertex
        self.neighbors = []

    def getWeight(self):
        return self.weight

    def getNeighbors(self):
        return self.neighbors

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def changeWeight(self, weight):
        self.weight = weight


class Edge:

    def __init__(self, prevNode, nextNode, weight):
        self.weight = weight
        # Technically there is no concept of previous and next node for
        # Undirected Graphs
        self.prevNode = prevNode
        self.nextNode = nextNode

    def getWeight(self):
        return self.weight

    def getPrevNode(self):
        return self.prevNode

    def getNextNode(self):
        return self.nextNode

    def changeWeight(self, weight):
        self.weight = weight
