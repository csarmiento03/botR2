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

    def __init__(self, cellSize, mediaFilename):
        self.maze = maze
        self.cellSize = cellSnumRowsize
        self.height = maze.numRows * cellSize
        self.width = maze.numCols * cellSize
        self.ax = None
        self.mediaFilename = mediaFilename

    def setMediaFilename(self, filename, mazeFilename):
        """Setea el atributo mediaFilename
            Argumentos:
                + filename (string): El nombre para los archivos y graficos
                + mazeFilename (string): Nombre del archivo que tiene guardada la matriz del laberinto
        """
        self.mediaFilename = filename

    def showMaze(self):
        """Grafica el laberinto pelado"""

        # Crea la figura y el estilo de los ejes
        fig = self.configurePlot()

        # Graficamos las paredes
        self.plotWalls()

        # Mostramos el grafico
        plt.show()

        # Handle any potential saving


    def plotWalls(self):
        """ Plots the walls of a maze. This is used when generating the maze image"""
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                if self.maze.initial_grid[i][j].is_entry_exit == "entry":
                    self.ax.text(j*self.cell_size, i*self.cell_size, "START", fontsize=7, weight="bold")
                elif self.maze.initial_grid[i][j].is_entry_exit == "exit":
                    self.ax.text(j*self.cell_size, i*self.cell_size, "END", fontsize=7, weight="bold")
                if self.maze.initial_grid[i][j].walls["top"]:
                    self.ax.plot([j*self.cell_size, (j+1)*self.cell_size],
                                 [i*self.cell_size, i*self.cell_size], color="k")
                if self.maze.initial_grid[i][j].walls["right"]:
                    self.ax.plot([(j+1)*self.cell_size, (j+1)*self.cell_size],
                                 [i*self.cell_size, (i+1)*self.cell_size], color="k")
                if self.maze.initial_grid[i][j].walls["bottom"]:
                    self.ax.plot([(j+1)*self.cell_size, j*self.cell_size],
                                 [(i+1)*self.cell_size, (i+1)*self.cell_size], color="k")
                if self.maze.initial_grid[i][j].walls["left"]:
                    self.ax.plot([j*self.cell_size, j*self.cell_size],
                                 [(i+1)*self.cell_size, i*self.cell_size], color="k")



class mazeForVisualization(object):

    """Clase guarda el laberinto para visualizar.

    Atributos: que lleva la visualización

        + fileName (string): El archivo donde esta guerdado el laberinto de la simulacion
        + maze: (2-D np.array) El laberinto que va a ser visualizado.
        + numRows (int): Numero de filas que tiene el laberinto
        + numCols (int): Numero de columnas que tiene el laberinto
        + entryCell (list): Coordenada de la celda de comienzo del laberinto
        + exitCell (list): Coordenada de la celda de salida del laberinto

    """

    def __init__(self, fileName):

        self.fileName = fileName
        self.maze = None
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
            self.maze = temp
            self.numRows = len(temp)
            self.numCols = len(temp[0])
            print("Laberinto guardado correctamente")
        else:
            self.entryCell = None
            self.exitCell = None
            print("El archself.numRowsivo de entrada no es un archivo valido")

    def getMaze(self):
        """Retorna la matriz del laberinto """
        return self.maze

    def getRowCol(self):
        """Retorna tupla con los valores de cantidad de filas y columnas que tiene el laberinto """
        return (self.numRows, self.numCols)

    def getEntry(self):
        """Retorna la posicion de la entrada """
        return self.entryCell

    def getExit(self):
        """Retorna la posicion de la salida """
        return self.exitCell
