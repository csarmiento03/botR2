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
        + cellSize (int): Que tan grande va a ser el laberinto
        + height (int): El largo del laberinto
        + width (int): El ancho del laberinto
        + ax: Los ejes para el plot.
        + mediaFilename (string): El nombre para los archivos y graficos

    """

    def __init__(self, maze, bot, cellSize, mediaFilename="resolucion"):
        self.maze = maze
        self.bot = bot
        self.cellSize = cellSize
        self.height = (maze.getRowCol())[0] * cellSize
        self.width = (maze.getRowCol())[1] * cellSize
        self.mediaFilename = mediaFilename
        self.ax = None

    def animator(self, mazeTuple=(True, "k", "palegreen", "lightcoral"), fps=15):
        """Generador del video de la animacion
            Argumentos:
                + mazeTuple (tupla): Tupla para configurar los detalles esteticos del laberinto
                    + Pos0 - xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                    + Pos1 - colorWall (str): Color de las paredes del lab. (Default negro)
                    + Pos2 - entryColor (str): Color de la entrada. (Default palegreen)
                    + Pos3 - exitColor (str): Color de la salida. (Default lightcoral)
                + fps (int): Cuadros por segundo de animacion
        """
        #Funcion interna para generar el video
        def updatefig(i):

            #Borra el robot
            self.bot.removeBot(self.ax)

            #Ubicamos al robot
            col = self.bot.getPos()[1]
            numRows = (self.maze.getRowCol())[0]
            row = (numRows - self.bot.getPos()[0] - 1)
            print("Cuadro " + str(i) + " de " + str(self.bot.getMaxFrame()))
            # Dibujamos el bot
            self.bot.drawBot(row, col, self.bot.getOrientation(), self.cellSize, self.ax)
            #Avanzamos un cuadro al bot para la siguiente iteracion
            self.bot.nextFrame()

            plt.draw()


        # Configuracion
        fig = self.configurePlot(xkcd=mazeTuple[0])
        # Graficamos las paredes
        self.plotWalls(colorWall=mazeTuple[1], entryColor=mazeTuple[2], exitColor=mazeTuple[3])
        # Graficamos el bot por primera vez en cualquier lado
        self.bot.drawBot(0, 0, 0, self.cellSize, self.ax)
        #Animamos usando la funcion updatefig()
        anim = animation.FuncAnimation(fig, updatefig, self.bot.getMaxFrame())
        #Guardamos la animacion
        file = self.mediaFilename + ".mp4"
        anim.save(file, fps=fps)

        # Lo movemos de vuelva al inicio
        self.bot.gotoSpecificFrame(frame=0)

    def showMaze(self, xkcd=True, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """Grafica el laberinto pelado
            Argumentos:
                + xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        # Crea la figura y el estilo de los ejes
        fig = self.configurePlot(xkcd=xkcd)

        # Graficamos las paredes
        self.plotWalls(colorWall, entryColor, exitColor)

        # Mostramos el grafico
        file = self.mediaFilename + "_maze.png"
        plt.savefig(file)
        plt.show()

    def showMazeWithBot(self, frame=0, xkcd=True, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """Grafica el laberinto con el bot en la posicion que esta el bot
            Argumentos:
                + frame (int) : En que cuadro se quiere dibujar el bot
                + xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        # Crea la figura y el estilo de los ejes
        fig = self.configurePlot(xkcd=xkcd)

        # Graficamos las paredes
        self.plotWalls(colorWall, entryColor, exitColor)

        #Ponemos el bot en una posicion especifica
        self.bot.gotoSpecificFrame(frame=frame)

        col = self.bot.getPos()[1]
        numRows = (self.maze.getRowCol())[0]
        row = (numRows - self.bot.getPos()[0] - 1)

        # Lo dibujamos
        self.bot.drawBot(row, col, self.bot.getOrientation(), self.cellSize, self.ax)
        # Lo movemos de vuelva al inicio
        self.bot.gotoSpecificFrame(frame=0)

        # Mostramos el grafico
        file = self.mediaFilename + "_frame" + str(frame) +".png"
        plt.savefig(file)
        plt.show()



    def showMazeWithResolution(self, xkcd=True, colorWall="k", entryColor="palegreen" ,exitColor="lightcoral"):
        """Generador del video de la animacion
            Argumentos:
                + xkcd (bool): Habilitar el estilo xkcd. Default:Habilitado
                + colorWall (str): Color de las paredes del lab. (Default negro)
                + entryColor (str): Color de la entrada. (Default palegreen)
                + exitColor (str): Color de la salida. (Default lightcoral)
        """
        # Crea la figura y el estilo de los ejes
        fig = self.configurePlot(xkcd=xkcd)

        # Graficamos las paredes
        self.plotWalls(colorWall, entryColor, exitColor)

        for i in range(self.bot.getMaxFrame()):

            col = self.bot.getPos()[1]
            numRows = (self.maze.getRowCol())[0]
            row = (numRows - self.bot.getPos()[0] - 1)

            self.bot.drawBot(row, col, self.bot.getOrientation(), self.cellSize, self.ax)
            self.bot.nextFrame()

        # Mostramos el grafico
        file = self.mediaFilename + "_resolution.png"
        plt.savefig(file)
        plt.show()

        # Lo movemos de vuelva al inicio
        self.bot.gotoSpecificFrame(frame=0)

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
        + publicPath (2-D np.array): Estructura de numpy con el camino recorrido y las orientaciones del bot pero ya suavizado para animarse
        + pos (tuple): Tupla que guarda en que casillero del laberinto esta el robot
        + orientation (int): Orientacion que tiene el robot
        + _maxKeyframe (int): El ultimo paso del recorrido del robot.
        + _actualKeyframe (int): En que paso está el robot.
        + actualFrame (int): En que paso está el robot cuando recorre el camino smooth.
        + maxFrame (int): El ultimo paso del recorrido del robot en el camino smooth.
    """
    def __init__(self):

        self._path = None
        self.publicPath = None
        self.pos = None
        self.orientation = None
        self._maxKeyframe = None
        self._actualKeyframe = None
        self.actualFrame = None
        self.maxFrame = None

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
            else:
                if (row[2] == 0):
                    row[2] = 0
                elif(row[2] == 1):
                    row[2] = 90
                elif(row[2] == 2):
                    row[2] = 180
                else:
                    row[2] = 270

        if (noError == True):
            self._path = path
            self.publicPath = self._path
            self.pos = (path[0][0], path[0][1])
            self.orientation = path[0][2]
            self._maxKeyframe = len(path) - 1
            self._actualKeyframe = 0
            self.maxFrame = self._maxKeyframe
            self.actualFrame = self._actualKeyframe
            print("Camino recorrido del bot guardado correctamente")
        else:
            self._path = None
            self.pos = None
            self.orientation = None
            self._maxKeyframe = None
            self._actualKeyframe = None
            self.maxFrame = None
            self.actualFrame = None
            print("El archivo de entrada no es un archivo valido")

    def smoothingPath(self, frames=10):
        """Metodo que obtiene el camino recorrido por el bot de forma suavizada

            Argumentos:
                + frames (int): Numero de cuadro entre los keyframes
        """
        #Dejamos parado en la parte inicial del laberinto un rato al bot
        smoothPath = np.tile(self._path[0], (frames, 1))

        for index in range(self._maxKeyframe):
            rowStart = self._path[index][0]*1.0
            colStart = self._path[index][1]*1.0
            orientationStart = self._path[index][2]*1.0
            rowEnd = self._path[index+1][0]*1.0
            colEnd = self._path[index+1][1]*1.0
            orientationEnd = self._path[index+1][2]*1.0

            #Realizamos un movimiento suave en el movimiento
            rows = np.linspace(rowStart, rowEnd, num=frames)
            cols = np.linspace(colStart, colEnd, num=frames)

            #Para la orientacion hay que tener cuidado con el tema de angulos y
            #como se hace para girar de izquierda a derecha o viceversa.
            if (orientationStart - orientationEnd) == -270:
                orientations = np.linspace(0, -90, num=frames)
            elif (orientationStart - orientationEnd) == 270:
                orientations = np.linspace(-90, 0, num=frames)
            else:
                orientations = np.linspace(orientationStart, orientationEnd, num=frames)

            #Unimos todos los movimientos
            union = np.array([rows, cols, orientations])
            union = union.T

            smoothPath = np.append(smoothPath, union, axis=0)

        #Dejamos parado en la parte final del laberinto un rato al bot
        ending = np.tile(self._path[-1], (2*frames, 1))

        smoothPath = np.append(smoothPath, ending, axis=0)

        self.publicPath = smoothPath
        self.actualFrame = 0
        self.maxFrame = len(smoothPath) - 1

    def nextFrame(self):
        """Metodo que modifica los datos del bots en posicion y orientacion usando los frames desde publicPath."""

        if (self.actualFrame < self.maxFrame):
            self.actualFrame += 1
            self.pos = (self.publicPath[self.actualFrame][0], self.publicPath[self.actualFrame][1])
            self.orientation = self.publicPath[self.actualFrame][2]

    def gotoSpecificFrame(self, frame=0):
        """Metodo que modifica los datos del bots en posicion y orientacion usando los frames desde publicPath.
        en una posicion especifica.
            Argumentos:
                + frame (int): Que cuadro especifico se quiere ir
        """
        self.actualFrame = frame
        self.pos = (self.publicPath[frame][0], self.publicPath[frame][1])
        self.orientation = self.publicPath[frame][2]

    def getPos(self):
        """Metodo que devuelve la posicion del bot

        """
        return self.pos

    def getOrientation(self):
        """Metodo que devuelve la orientacion del bot

        """
        return self.orientation

    def getActualFrame(self):
        """Metodo que devuelve en que frame está

        """
        return self.actualFrame

    def getMaxFrame(self):
        """Metodo que devuelve en cual es el ultimo keyframe

        """
        return self.maxFrame

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

    def removeBot(self, axes):
        """Metodo borra el bot
            Argumentos:
                + axes (matplotlib axes): Ejes donde se dibuja el bot
        """
        self.drawing.remove()

    def changeColor(self, color):
        """Metodo cambia color del bot
            Argumentos:
                + color (str): Color a cambiar
        """
        self.faceColor = color
