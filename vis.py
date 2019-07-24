import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

    def showMaze(self, xkcd=True, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """Grafica el laberinto pelado
            Argumentos:
                + xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        # Crea la figura y el estilo de los ejes
        tfig = self.configurePlot(xkcd)

        # Graficamos las paredes
        self.plotWalls(colorWall, entryColor, exitColor)

        # Mostramos el grafico
        plt.show()

        # Handle any potential saving


    def plotWalls(self, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """ Grafica las paredes del laberinto
            Argumentos:
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        #Obtenemos el numero de fila y columnas tiene el laberinto
        numRows = (self.maze.getRowCol())[0]
        numCol = (self.maze.getRowCol())[1]
        # Y la estructura del laberinto
        mazeStructure = self.maze.getMaze()

        for i in range(numRows):
            for j in range(numCol):

                indexRow = numRows - i - 1
                indexCol = j

                # Si hay una pared a la izquierda
                if mazeStructure[i][j] & 1 > 0:
                    self.ax.plot([indexCol*self.cellSize, indexCol*self.cellSize],
                                 [indexRow*self.cellSize, (indexRow+1)*self.cellSize],
                                 color=colorWall, linewidth=3)
                # Si hay una pared a arriba
                if mazeStructure[i][j] & 2 > 0:
                    self.ax.plot([(indexCol+1)*self.cellSize, indexCol*self.cellSize],
                                 [(indexRow+1)*self.cellSize, (indexRow+1)*self.cellSize],
                                 color=colorWall, linewidth=3)
                # Si hay una pared a la derecha
                if mazeStructure[i][j] & 4 > 0:
                    self.ax.plot([(indexCol+1)*self.cellSize, (indexCol+1)*self.cellSize],
                                 [indexRow*self.cellSize, (indexRow+1)*self.cellSize],
                                 color=colorWall, linewidth=3)
                # Si hay una pared abajo
                if mazeStructure[i][j] & 8 > 0:
                    self.ax.plot([(indexCol+1)*self.cellSize, indexCol*self.cellSize],
                                 [indexRow*self.cellSize, indexRow*self.cellSize],
                                 color=colorWall, linewidth=3)


        #Graficamos la entrada y salida de laberinto
        mazeEntry = self.maze.getEntry()
        xEntry = mazeEntry[1]*self.cellSize
        yEntry = (numRows - mazeEntry[0] - 1)*self.cellSize

        rectEntry = mpatches.Rectangle((xEntry, yEntry), self.cellSize, self.cellSize,
                    facecolor=entryColor)
        self.ax.add_patch(rectEntry)

        mazeExit = self.maze.getExit()
        xExit = mazeExit[1]*self.cellSize
        yExit = (numRows - mazeExit[0] - 1)*self.cellSize

        rectExit = mpatches.Rectangle((xExit, yExit), self.cellSize, self.cellSize,
                facecolor=exitColor)
        self.ax.add_patch(rectExit)

    def configurePlot(self, xkcd=True):
        """Setea las configuraciones iniciales del plot. Ademas crea el plot y los ejes
            Argumentos:
                + xkcd (bool): Habilitar un estilo xkcd(). Default:Enable
        """

        numRows = (self.maze.getRowCol())[0]
        numCol = (self.maze.getRowCol())[1]

        # Create the plot figure
        if (xkcd == True):
            plt.xkcd()
        else:
            plt.rcdefaults()

        fig = plt.figure(figsize = (7, 7*numRows/numCol))

        # Create the axes
        self.ax = plt.axes()

        # Set an equal aspect ratio
        self.ax.set_aspect("equal")

        # Remove the axes from the figure
        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)

        return fig


class MazeForVisualization(object):

    """Clase guarda el laberinto para visualizar.

    Atributos:

        + structure: (2-D np.array) La estructura del laberinto que va a ser visualizado.
        + numRows (int): Numero de filas que tiene el laberinto
        + numCols (int): Numero de columnas que tiene el laberinto
        + entryCell (list): Coordenada de la celda de comienzo del laberinto
        + exitCell (list): Coordenada de la celda de salida del laberinto

    """

    def __init__(self):

        self.structure = None
        self.numRows = None
        self.numCols = None
        self.entryCell = None
        self.exitCell = None

    def loadMazeFile(self, fileName):
        """Carga el archivo del laberintos

            Argumentos:
                + fileName (string): El archivo donde esta guardado el laberinto de la simulacion
         """

        temp = np.load(fileName) #Variable temporal que va a guardar el numpy array qeu se obtiene de leer el archivo

        noError = True #Flag que indica que se cargo todo correctamente

        #Chequeamos que el archivo tiene valores esperados
        for indexRow, row in enumerate(temp):
            for indexCol, cellValue in enumerate(row):
                if cellValue > 63 or cellValue < 0: #Esto no es un laberinto
                    noError = False
                    break
                elif cellValue > 15:
                    if (cellValue & 16 > 0): #Vemos si es una entrada
                        self.entryCell = (indexRow, indexCol)
                    if (cellValue & 32 > 0): #Vemos si es una salida
                        self.exitCell = (indexRow, indexCol)
                    temp[indexRow][indexCol] = cellValue & 15 #Quitamos la informacion de si es salida o entrada

        if (noError == True):
            self.structure = temp
            self.numRows = len(temp)
            self.numCols = len(temp[0])
            print("Laberinto guardado correctamente")
        else:
            self.entryCell = None
            self.exitCell = None
            print("El archivo de entrada no es un archivo valido")

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

#class BotForVisualization(object):

#    """Clase que dibuja el bot que recorre el camino de la simulacion.
#
#    Atributos: que lleva la visualización
#
#        + path (2-D np.array): Estructura de numpy con el camino recorrido y las orientaciones del bot
#
#    """
#    def __init__(self):
#
#        self.path = None
#
#    def loadPath(self, filename):
#        """Metodo que carga el archivo con el camino recorrido por el bot.
#
#            Argumentos:
#                + fileName (string): El archivo donde esta guardado el camino
#        """
#
##            temp = np.load(filename) #Variable temporal que va a guardar el numpy array qeu se obtiene de leer el archivo
#
#            noError = True #Flag que indica que se cargo todo correctamente
#            np.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None)[source]¶
#            #Chequeamos que el archivo tiene valores esperados
#            for indexRow, row in enumerate(temp):
#                for indexCol, cellValue in enumerate(row):
#                    if cellValue > 63 or cellValue < 0: #Esto no es un laberinto
#                        noError = False
#                        break
#                    elif cellValue > 15:
#                        if (cellValue & 16 > 0): #Vemos si es una entrada
#                            self.entryCell = (indexRow, indexCol)
#                        if (cellValue & 32 > 0): #Vemos si es una salida
#                            self.exitCell = (indexRow, indexCol)
#                        temp[indexRow][indexCol] = cellValue & 15 #Quitamos la informacion de si es salida o entrada
#
#            if (noError == True):
#                self.structure = temp
#                self.numRows = len(temp)
#                self.numCols = len(temp[0])
#                print("Laberinto guardado correctamente")
#            else:
#                self.entryCell = None
#                self.exitCell = None
#                print("El archself.numRowsivo de entrada no es un archivo valido")


#class TriangleBot(BotForVisualization):
#
#    """Clase dibuja el bot que recorre el camino de la simulacion.

#    Atributos: que lleva la visualización
#
#        + fileName (string): El archivo donde esta guardado el camino
#        + structure: (2-D np.array) La estructura del laberinto que va a ser visualizado.
#        + numRows (int): Numero de filas que tiene el laberinto
#        + numCols (int): Numero de columnas que tiene el laberinto
#        + entryCell (list): Coordenada de la celda de comienzo del laberinto
#        + exitCell (list): Coordenada de la celda de salida del laberinto

#    """
    #def __init__(self):

    #    self.structure = None
    #    self.numRows = None
    #    self.numCols = None
    #    self.entryCell = None
    #    self.exitCell = None

    #def drawBot(self, pos, angleRotation):
    #    """Metodo dibuja el bot en una posicion y con una rotacion dada.
    #
    #        Argumentos:
    #            + pos (string): tupla con la posicion donde debe dibujar el robot
    #            + angleRotation: Angulo de orientacion que debe dibujar el bot.
    #
    #    """


    #def loadPath(self, filename):
    #    """Metodo que carga el archivo con el camino recorrido por el bot.
    #
    #        Argumentos:
    #            + fileName (string): El archivo donde esta guardado el camino
    #    """
