import numpy as np
import matplotlib.pyplot as plt

class Visualizer(object):
    """Clase que lleva la visualización.

    Atributos:

        + maze: (obj mazeForVisualization) Objeto de laberinto que va a ser visualizado.
        + cellSize (int): Que tan grande va a ser el laberinto
        + height (int): El largo del laberinto
        + width (int): El ancho del laberinto
        + ax: Los ejes para el plot.
        + mediaFilename (string): El nombre para los archivos y graficos

    """

    def __init__(self, maze, cellSize, mediaFilename):
        self.maze = maze
        self.cellSize = cellSize
        self.height = (maze.getRowCol())[0] * cellSize
        self.width = (maze.getRowCol())[1] * cellSize
        self.ax = None

    def setMediaFilename(self, filename):
        """Setea el atributo mediaFilename
            Argumentos:
                + filename (string): El nombre para los archivos y graficos
        """
        self.mediaFilename = filename

    def showMaze(self):
        """Grafica el laberinto pelado"""

        # Crea la figura y el estilo de los ejes
        tfig = self.configurePlot()

        # Graficamos las paredes
        self.plotWalls()

        # Mostramos el grafico
        plt.show()

        # Handle any potential saving


    def plotWalls(self):
        """ Grafica las paredes del laberinto"""

        #Obtenemos el numero de fila y columnas tiene el laberinto
        numRows = (self.maze.getRowCol())[0]
        numCol = (self.maze.getRowCol())[1]
        # Y la estructura del laberinto
        mazeStructure = self.maze.getMaze()

        print(mazeStructure)

        for i in range(numRows):
            for j in range(numCol):

                indexRow = numRows - i - 1
                indexCol = j

                # Si hay una pared a la izquierda
                if mazeStructure[i][j] & 1 > 0:
                    self.ax.plot([indexCol*self.cellSize, indexCol*self.cellSize],
                                 [indexRow*self.cellSize, (indexRow+1)*self.cellSize], color="k")
                # Si hay una pared a arriba
                if mazeStructure[i][j] & 2 > 0:
                    self.ax.plot([j*self.cellSize, (j+1)*self.cellSize],
                                 [(indexRow+1)*self.cellSize, (indexRow+1)*self.cellSize], color="r")
                # Si hay una pared a la derecha
                if mazeStructure[i][j] & 4 > 0:
                    self.ax.plot([(indexCol+1)*self.cellSize, (indexCol+1)*self.cellSize],
                                 [indexRow*self.cellSize, (indexRow+1)*self.cellSize], color="b")
                # Si hay una pared abajo
                if mazeStructure[i][j] & 8 > 0:
                    self.ax.plot([(indexCol+1)*self.cellSize, indexCol*self.cellSize],
                                 [indexRow*self.cellSize, indexRow*self.cellSize], color="m")

                #if self.maze.initial_grid[i][j].is_entry_exit == "entry":
                #    self.ax.text(j*self.cell_size, i*self.cell_size, "START", fontsize=7, weight="bold")
                #elif self.maze.initial_grid[i][j].is_entry_exit == "exit":
                #    self.ax.text(j*self.cell_size, i*self.cell_size, "END", fontsize=7, weight="bold")

    def configurePlot(self):
        """Setea las configuraciones iniciales del plot. Ademas crea el plot y los ejes"""

        numRows = (self.maze.getRowCol())[0]
        numCol = (self.maze.getRowCol())[1]

        # Create the plot figure
        fig = plt.figure(figsize = (7, 7*numRows/numCol))

        # Create the axes
        self.ax = plt.axes()

        # Set an equal aspect ratio
        self.ax.set_aspect("equal")

        # Remove the axes from the figure
        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)

        title_box = self.ax.text(0, numRows + numCol + 0.1,
                            r"{}$\times${}".format(numRows, numCol),
                            bbox={"facecolor": "gray", "alpha": 0.5, "pad": 4}, fontname="serif", fontsize=15)

        return fig


class MazeForVisualization(object):

    """Clase guarda el laberinto para visualizar.

    Atributos: que lleva la visualización

        + fileName (string): El archivo donde esta guerdado el laberinto de la simulacion
        + structure: (2-D np.array) La estructura del laberinto que va a ser visualizado.
        + numRows (int): Numero de filas que tiene el laberinto
        + numCols (int): Numero de columnas que tiene el laberinto
        + entryCell (list): Coordenada de la celda de comienzo del laberinto
        + exitCell (list): Coordenada de la celda de salida del laberinto

    """

    def __init__(self, fileName):

        self.fileName = fileName
        self.structure = None
        self.numRows = None
        self.numCols = None
        self.entryCell = None
        self.exitCell = None

    def loadMazeFile(self):
        """Carga el archivo del laberintos """

        temp = np.load(self.fileName) #Variable temporal que va a guardar el numpy array qeu se obtiene de leer el archivo

        noError = True #Flag que indica que se cargo todo correctamente

        #Chequeamos que el archivo tiene valores esperados
        for indexRow, row in enumerate(temp):
            for indexCol, cellValue in enumerate(row):
                if cellValue > 63 or cellValue < 0: #Esto no es un laberinto
                    noError = False
                    break
                elif cellValue > 15:
                    if (cellValue & 16 > 0): #Vemos si es una entrada
                        self.entryCell = [indexRow, indexCol]
                    if (cellValue & 32 > 0): #Vemos si es una salida
                        self.exitCell = [indexRow, indexCol]
                    temp[indexRow][indexCol] = cellValue & 15 #Quitamos la informacion de si es salida o entrada

        if (noError == True):
            self.structure = temp
            self.numRows = len(temp)
            self.numCols = len(temp[0])
            print("Laberinto guardado correctamente")
        else:
            self.entryCell = None
            self.exitCell = None
            print("El archself.numRowsivo de entrada no es un archivo valido")

    def getMaze(self):
        """Retorna la matriz del laberinto """
        return self.structure

    def getRowCol(self):
        """Retorna tupla con los valores de cantidad de filas y columnas que tiene el laberinto """
        return (self.numRows, self.numCols)

    def getEntry(self):
        """Retorna la posicion de la entrada """
        return self.entryCell

    def getExit(self):
        """Retorna la posicion de la salida """
        return self.exitCell
