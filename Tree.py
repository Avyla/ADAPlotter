class Node:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        self.son = []

    def addSon(self, son):
        self.son.append(son)


class Tree:
    def __init__(self, coordinates):
        self.root = Node(coordinates, "Coordinates")

    def findNode(self, figureType):
        return self._findNode(self.root, figureType)

    def _findNode(self, currentNode, figureType):
        if currentNode.type == figureType:
            return currentNode

        for son in currentNode.son:
            result = self._findNode(son, figureType)
            if result:
                return result
        return None

    def createTree(self, listFigures):
        for figure in listFigures:
            nodeArea = Node(figure.getArea(), 'Area')
            for coordinate in figure.getCoordinates():
                nodeArea.addSon(Node(coordinate, 'Coordinate'))

            result = self.findNode(figure.getFigureType())
            if result:
                result.addSon(nodeArea)
            else:
                newNode = Node(0, figure.getFigureType())
                newNode.addSon(nodeArea)
                self.root.addSon(newNode)

    def showTree(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.root

        space = '  ' * nivel
        print(space + f"{nodo.type}: {nodo.value}")
        for son in nodo.son:
            self.showTree(son, nivel + 1)
