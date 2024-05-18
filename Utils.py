import ast
import math
import itertools

from Figure import Figure


class Utils:
    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    @staticmethod
    def hypotenuse(listDistances):
        sortedDistances = sorted(listDistances)
        a, b, c = sortedDistances
        c = round((c ** 2), 2)
        a = round((a ** 2), 2)
        b = round((b ** 2), 2)
        return c == a + b

    @staticmethod
    def distanceOpposite(listDistance):
        if listDistance[0] != listDistance[2] or listDistance[1] != listDistance[3]:
            return False
        return True

    @staticmethod
    def earringOpposite(listPoints):
        try:
            earring1 = (listPoints[1][1] - listPoints[0][1]) / (listPoints[1][0] - listPoints[0][0])
        except ZeroDivisionError:
            earring1 = float('inf')

        try:
            earring2 = (listPoints[3][1] - listPoints[2][1]) / (listPoints[3][0] - listPoints[2][0])
        except ZeroDivisionError:
            earring2 = float('inf')

        return earring1 == earring2

    @staticmethod
    def generateCombinations(coordinates, num):
        return itertools.combinations(coordinates, num)

    @staticmethod
    def calcDistances(combination):
        return [Utils.distance(combination[i], combination[i + 1]) for i in range(len(combination) - 1)] + [
            Utils.distance(combination[-1], combination[0])]

    @staticmethod
    def areaTriangle(listCoordinates):
        distances = Utils.calcDistances(listCoordinates)
        a, b, c = sorted(distances)
        return (a * b) / 2

    @staticmethod
    def areaSquare(listCoordinates):
        distances = Utils.calcDistances(listCoordinates)
        return distances[0] ** 2

    @staticmethod
    def areaRectangle(listCoordinates):
        distances = Utils.calcDistances(listCoordinates)
        return distances[0] * distances[2]

    @staticmethod
    def findRectangle(coordinates, toStore):
        combinations = list(Utils.generateCombinations(coordinates, 4))
        for combination in combinations:
            distances = Utils.calcDistances(combination)
            if len(set(distances)) == 2 and Utils.distanceOpposite(distances) and Utils.earringOpposite(combination):
                toStore.append(Figure('Rectangle', Utils.areaRectangle(combination), combination))

    @staticmethod
    def findSquare(coordinates, toStore):
        combinations = list(Utils.generateCombinations(coordinates, 4))
        for combination in combinations:
            distances = Utils.calcDistances(combination)
            if len(set(distances)) == 2 and Utils.distanceOpposite(distances) and Utils.earringOpposite(combination):
                toStore.append(Figure('Square', Utils.areaSquare(combination), combination))

    @staticmethod
    def findTriangle(coordinates, toStore):
        combinations = list(Utils.generateCombinations(coordinates, 3))
        for combination in combinations:
            distances = Utils.calcDistances(combination)
            if Utils.hypotenuse(distances):
                toStore.append(Figure('Triangle', Utils.areaTriangle(combination), combination))

    @staticmethod
    def parseCoordinates(strCoordinate):
        try:
            coordinates = ast.literal_eval(strCoordinate)
            if isinstance(coordinates, list) and all(
                    isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
                return coordinates
            else:
                raise ValueError("Incorrect coordinate format.")
        except (SyntaxError, ValueError):
            raise ValueError("Incorrect coordinate format.")

