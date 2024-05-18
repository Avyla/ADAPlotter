class Figure:
    def __init__(self, figureType, area, coordinates):
        self.figureType = figureType
        self.area = area
        self.coordinates = coordinates

    def getFigureType(self):
        return self.figureType

    def getArea(self):
        return self.area

    def getCoordinates(self):
        return self.coordinates

