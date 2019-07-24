import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl
import matplotlib.animation as animation

class Visualizer(object):
    """Clase que lleva la visualización.

    Atributos:

        + maze (obj mazeForVisualization): Objeto de laberinto que va a ser visualizado.
        + bot (obj hijos de BotForVisualization): Objeto del bot que va a ser visualizado.
        + deltaTime (int): Delta de tiempo que se va ejecutar cada cuadro de la simulacion
        + smoother (int): Numero que indica cuantos cuadros habra entre cada keyframe.
        + cellSize (int): Que tan grande va a ser el laberinto
        + height (int): El largo del laberinto
        + width (int): El ancho del laberinto
        + ax: Los ejes para el plot.
        + mediaFilename (string): El nombre para los archivos y graficos

    """

    def __init__(self, maze, bot, cellSize, deltaTime, smoother, mediaFilename):
        self.maze = maze
        self.bot = bot
        self.cellSize = cellSize
        self.height = (maze.getRowCol())[0] * cellSize
        self.width = (maze.getRowCol())[1] * cellSize
        self.ax = None

    def animator(self, mazeTuple=(True, "k", "palegreen", "lightcoral")):


        def updatefig(i):

            fig.clear()

            aa = self.configurePlot(createFigure=False, xkcd=mazeTuple[0])

            # Graficamos las paredes
            self.plotWalls(colorWall=mazeTuple[1], entryColor=mazeTuple[2], exitColor=mazeTuple[3])

            col = self.bot.getPos()[1]
            numRows = (self.maze.getRowCol())[0]
            row = (numRows - self.bot.getPos()[0] - 1)
            self.bot.drawBot(row, col, self.bot.getOrientation(), self.cellSize, self.ax)
            self.bot.nextKeyframe()
            plt.draw()

        fig = self.configurePlot(createFigure=True, xkcd=mazeTuple[0])
        anim = animation.FuncAnimation(fig, updatefig, self.bot.getMaxKeyframe()+20)
        anim.save("test.mp4", fps=3)



    def showMaze(self, xkcd=True, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """Grafica el laberinto pelado
            Argumentos:
                + xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        # Crea la figura y el estilo de los ejes
        fig = self.configurePlot(xkcd)

        # Graficamos las paredes
        self.plotWalls(colorWall, entryColor, exitColor)

        #col = self.bot.getPos()[1]
        #numRows = (self.maze.getRowCol())[0]
        #row = (numRows - self.bot.getPos()[0] - 1)

        #self.bot.drawBot(row, col, self.bot.getOrientation(), self.cellSize, self.ax)

        # Mostramos el grafico
        plt.show()


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

    def configurePlot(self, createFigure=True, xkcd=True):
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

        if (createFigure == True):
            fig = plt.figure(figsize = (7, 7*numRows/numCol))
        else:
            fig = None

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
         #Variable temporal que va a guardar el numpy array qeu se obtiene de leer el archivo
        temp = np.loadtxt(fileName, dtype=int, comments='#', delimiter=",", skiprows=0)

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

class BotForVisualization(object):

    """Clase que dibuja el bot que recorre el camino de la simulacion.

    Atributos: que lleva la visualización

        + path (2-D np.array): Estructura de numpy con el camino recorrido y las orientaciones del bot
        + pos (tuple): Tupla que guarda en que casillero del laberinto esta el robot
        + orientation (int): Orientacion que tiene el robot
        + maxKeyframe (int): El ultimo paso del recorrido del robot.
        + actualKeyframe (int): En que paso está el robot.

    """
    def __init__(self):

        self.path = None
        self.pos = None
        self.orientation = None
        self.maxKeyframe = None
        self.actualKeyframe = None

    def loadPath(self, filename):
        """Metodo que carga el archivo con el camino recorrido por el bot.

            Argumentos:
                + fileName (string): El archivo donde esta guardado el camino
        """

        #Variable temporal que va a guardar el numpy array qeu se obtiene de leer el archivo
        path = np.loadtxt(filename, dtype=int, comments='#', delimiter=",", skiprows=0)
        noError = True #Flag que indica que se cargo todo correctamente

        #Si el valor correspondiente a una orientacion no es dato valido (tiene que ser
        # entre 0 y 3)
        for row in path:
            if row[2] > 3 or row[2] < 0:
                noError = False
                break

        if (noError == True):
            self.path = path
            self.pos = (path[0][0], path[0][1])
            self.orientation = path[0][2]
            self.maxKeyframe = len(path) - 1
            self.actualKeyframe = 0
            print("Camino recorrido del bot guardado correctamente")
        else:
            self.path = None
            self.pos = None
            self.orientation = None
            self.maxKeyframe = None
            self.actualKeyframe = None
            print("El archivo de entrada no es un archivo valido")

    def nextKeyframe(self):
        """Metodo que modifica los datos del bots en posicion y orientacion.

        """
        if (self.actualKeyframe < self.maxKeyframe):
            self.actualKeyframe += 1
            self.pos = (self.path[self.actualKeyframe][0], self.path[self.actualKeyframe][1])
            self.orientation = self.path[self.actualKeyframe][2]

    def getPos(self):
        """Metodo que devuelve la posicion del bot

        """
        return self.pos

    def getOrientation(self):
        """Metodo que devuelve la orientacion del bot

        """
        if (self.orientation == 0):
            angle = 0
        elif(self.orientation == 1):
            angle = 90
        elif(self.orientation == 2):
            angle = 180
        else:
            angle = 270

        return angle

    def getActualKeyframe(self):
        """Metodo que devuelve en que keyframe está

        """
        return self.actualKeyframe

    def getMaxKeyframe(self):
        """Metodo que devuelve en cual es el ultimo keyframe

        """
        return self.maxKeyframe


class RegularPolygonBot(BotForVisualization):

    """Clase dibuja el bot que recorre el camino de la simulacion con una forma de poligono regular

    Atributos:

        + Hereda los atributos de la clase padre BotForVisualization
        + drawing (matplotlib.patches.RegularPolygon): Poligono regular de matplotlib (triangulo)
        + numVertices (int): Numero de vertices que tiene el poligono
        + faceColor (string): Color del poligono

    """
    def __init__(self, numVertices=3, faceColor="m"):

        self.drawing = None
        self.numVertices = numVertices
        self.faceColor = faceColor

    def drawBot(self, row, col, angleRotation, cellSize, axes):
        """Metodo dibuja el bot en una posicion y con una rotacion dada.

            Argumentos:
                + row (int): Fila que nos indica en que fila esta el bot
                + col (int): Fila que nos indica en que columna esta el bot
                + angleRotation (int): Angulo de orientacion que debe dibujar el bot.
                + cellSize (float): Tamaño de la celda a dibujar el robot
                + axes (matplotlib axes): Ejes donde se dibuja el bot

        """
        x = (col + 0.5)*cellSize
        y = (row + 0.5)*cellSize

        #Dibujamos el poligono
        polygon = mpatches.RegularPolygon((0, 0), self.numVertices, radius=cellSize/3, facecolor=self.faceColor)

        #Rotamos el poligono en los angulos pedidos
        t1 = mpl.transforms.Affine2D().rotate_deg(angleRotation)
        #Movemos el poligono a la posicion indicada
        t2 = mpl.transforms.Affine2D().translate(x, y)

        #Unimos todas las transformaciones
        tra = t1 + t2 + axes.transData
        polygon.set_transform(tra)

        self.drawing = polygon
        axes.add_patch(polygon)
