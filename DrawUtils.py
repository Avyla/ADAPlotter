import matplotlib.pyplot as plt


class DrawUtils:

    @staticmethod
    def drawFigure(Figures):
        for figure in Figures:
            coordinates = figure.getCoordinates()
            x_coords, y_coords = zip(*coordinates)
            plt.scatter(x_coords, y_coords, label=coordinates)
            plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],))
        plt.legend()
        plt.show()

    @staticmethod
    def drawCoordinates(coordinates):
        for coordinate in coordinates:
            x_coord, y_coord = coordinate
            plt.scatter(x_coord, y_coord, label=coordinate)
        plt.legend()
        plt.show()
