import tkinter as tk
from tkinter import messagebox
from DrawUtils import DrawUtils
from Tree import Tree
from Utils import Utils


class View:
    def __init__(self, root):
        self.root = root
        self.root.title('ADA Plotter')
        self.coordinates = []
        self.figures = []

        self.root.geometry("400x400")  # Ancho x Alto

        self.frameInitial = tk.Frame(self.root)
        self.frameInitial.pack()

        tk.Label(self.frameInitial, text='List of coordinates', width=20, height=2, padx=10, pady=5).pack()

        self.entryCoordinates = tk.Entry(self.frameInitial,
                                         width=20,
                                         font=5)
        self.entryCoordinates.pack()

        self.buttonVerify = tk.Button(self.frameInitial,
                                      text='Verify coordinates',
                                      command=self.verifyCoordinates,
                                      width=20,
                                      height=2,
                                      padx=10,
                                      pady=5)
        self.buttonVerify.pack()

        self.buttonCoordinates = tk.Button(self.frameInitial,
                                           text='Draw coordinates',
                                           command=self.drawCoordinates,
                                           state=tk.DISABLED,
                                           width=20,
                                           height=2,
                                           padx=10,
                                           pady=5)
        self.buttonCoordinates.pack()

        self.buttonTriangles = tk.Button(self.frameInitial,
                                         text='Draw triangles',
                                         command=self.drawTriangles,
                                         state=tk.DISABLED,
                                         width=20,
                                         height=2,
                                         padx=10,
                                         pady=5)
        self.buttonTriangles.pack()

        self.buttonSquares = tk.Button(self.frameInitial,
                                       text='Draw squares',
                                       command=self.drawSquares,
                                       state=tk.DISABLED,
                                       width=20,
                                       height=2,
                                       padx=10,
                                       pady=5)
        self.buttonSquares.pack()

        self.buttonRectangles = tk.Button(self.frameInitial,
                                          text='Draw Rectangles',
                                          command=self.drawRectangles,
                                          state=tk.DISABLED,
                                          width=20,
                                          height=2,
                                          padx=10,
                                          pady=5)
        self.buttonRectangles.pack()

        self.buttonTree = tk.Button(self.frameInitial,
                                    text='Show tree',
                                    command=self.showTree,
                                    state=tk.DISABLED,
                                    width=20,
                                    height=2,
                                    padx=10,
                                    pady=5)
        self.buttonTree.pack()

        self.buttonClear = tk.Button(self.frameInitial,
                                     text='Clear',
                                     command=self.clear,
                                     width=20,
                                     height=2,
                                     padx=10,
                                     pady=5)
        self.buttonClear.pack()

    def verifyCoordinates(self):
        newCoordinates = self.entryCoordinates.get()
        try:
            listCoordinates = Utils.parseCoordinates(newCoordinates)
            if not (len(listCoordinates) < 3):
                self.buttonCoordinates.config(state=tk.NORMAL)

                self.coordinates = listCoordinates
                Utils.findSquare(listCoordinates, self.figures)
                Utils.findTriangle(listCoordinates, self.figures)
                Utils.findRectangle(listCoordinates, self.figures)

                self.updateButton()

                messagebox.showinfo("Information", f'''Triangles found: {len(self.filterFiguresByType('Triangle'))}
Squares found: {len(self.filterFiguresByType('Square'))}
Rectangles found: {len(self.filterFiguresByType('Rectangle'))}''')

                self.buttonVerify.config(state=tk.DISABLED)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def drawTriangles(self):
        DrawUtils.drawFigure(self.filterFiguresByType('Triangle'))

    def drawSquares(self):
        DrawUtils.drawFigure(self.filterFiguresByType('Square'))

    def drawRectangles(self):
        DrawUtils.drawFigure(self.filterFiguresByType('Rectangle'))

    def drawCoordinates(self):
        DrawUtils.drawCoordinates(self.coordinates)

    def showTree(self):
        tree = Tree(self.coordinates)
        tree.createTree(self.figures)
        tree.showTree()

    def updateButton(self):
        self.buttonTriangles.config(state=tk.NORMAL if len(self.filterFiguresByType('Triangle')) > 0 else tk.DISABLED)
        self.buttonSquares.config(state=tk.NORMAL if len(self.filterFiguresByType('Rectangle')) > 0 else tk.DISABLED)
        self.buttonRectangles.config(state=tk.NORMAL if len(self.filterFiguresByType('Square')) > 0 else tk.DISABLED)
        self.buttonTree.config(state=tk.NORMAL if len(self.figures) > 0 else tk.DISABLED)

    def clear(self):
        self.buttonVerify.config(state=tk.NORMAL)
        self.entryCoordinates.delete(0, tk.END)
        self.buttonCoordinates.config(state=tk.DISABLED)
        self.buttonTriangles.config(state=tk.DISABLED)
        self.buttonSquares.config(state=tk.DISABLED)
        self.buttonRectangles.config(state=tk.DISABLED)
        self.buttonTree.config(state=tk.DISABLED)
        self.coordinates.clear()
        self.figures.clear()

    def filterFiguresByType(self, figureType):
        return [figure for figure in self.figures if figure.getFigureType() == figureType]


if __name__ == "__main__":
    root = tk.Tk()
    ventana = View(root)
    root.mainloop()
