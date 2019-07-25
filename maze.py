#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  maze.py

import numpy as np
import random
from cell import Cell



class Maze():
    """
    Clase 'Maze' genérica, solo es capaz de inicializar un laberinto.
    Atributos:
        grid: una lista de listas anidadas que conienen objetos 'Cell'.
        start: una tupla de enteros del tipo (y,x) ó (row, col).
        end: una tupla de enteros del tipo (y,x) ó (row, col).
    Invocación:
        size: Una tupla de enteros del tipo (y,x) ó (row, col).
              Definen las dimensiones de la 'grid'.
        walls: bool que indica si los objetos 'Cell' a inicializar
               tendrán las paredes activas por defecto o no.
    """

    def __init__(self, size, walls=True):
        self.size = size
        self.start = (0,0)
        self.end = (0,0)
        self.grid = list()

        # Inicializa 'grid' de acuerdo a 'size'.
        for i in range(size[0]):
            row = list()
            for j in range(size[1]):
                row.append(Cell(pos=(i,j), walls=walls))
            self.grid.append(row)

    def getStart(self):
        """
        Devuelve 'start'
        """
        return self.start

    def getEnd(self):
        """
        Devuelve 'end'
        """
        return self.end

    def getWalls(self, pos):
        """
        Devuelve una lista con información de las paredes 
        de una celda en posición 'pos'. ver Cell.getwalls().
        """
        try: return self.grid[pos[0]][pos[1]].getWalls()
        except: pass

    def saveMaze(self, fname):
        """
        Guarda el laberinto en un archivo de texto listo para
        ser levantado por 'vis.py'.
        fname: Nombre del archivo de texto.
        """
        size = (len(self.grid), len(self.grid[0]))
        data = np.zeros(size, dtype=int)
        for row in range(size[0]):
            for col in range(size[1]):
                data[row,col] = int(self.grid[row][col].sumWalls())
        data[self.start[0], self.start[1]] += 16
        data[self.end[0],self.end[1]] += 32
        np.savetxt(fname, data, delimiter=',', fmt="%d")


    def buildMaze(self, start=False, end=False):
        """
        Función dummy.
        """
        pass

class BoxMaze(Maze):

    def buildMaze(self, start=False, end=False):
        """
        Crea un laberinto trivial de tamaño "size" que consiste en
        una caja vacía. "start" y "end" son tuplas que pueden especificar
        la posición de la entrada y la salida del laberinto.
        """
        # Actualiza 'start' y 'end' de acuerdo a los argumentos.
        # Define variables auxiliares.

        size = self.size
        bottom = size[0] -1
        right = size[1] -1
        if start != False: self.start = start
        else: self.start = (0,0)
        if end != False: self.end = end
        else: self.end = (bottom, right)



        # Implementa un laberinto con forma de caja
        for i in range(size[0]):
            for j in range(size[1]):
                if j != right:
                    self.grid[i][j].wallE = False
                if j != 0: 
                    self.grid[i][j].wallW = False
                if i != bottom:
                    self.grid[i][j].wallS = False
                if i != 0:
                    self.grid[i][j].wallN = False

        # Implementa la entrada y salida.
        self.grid[start[0]][start[1]].wallN = False
        self.grid[start[0]][start[1]].start = True
        self.grid[end[0]][end[1]].wallS = False
        self.grid[end[0]][end[1]].end = True


class BacktrackingMaze(Maze):
    """
    Este laberinto implementa el algoritmo de recursive backtracking.
    Es un algoritmo sencillo que favorece corredores largos.
    No es muy eficiente en términos de memoria, pero funciona bien para
    laberintos no gigantes :)
    """

    def buildMaze(self, start=False, end=False):
        """
        Construye el laberinto de acuerdo al siguiente algoritmo:
        Inicio: 
            -Elige una celda al azar y la añade al stack
        Recursivo:
            -Elige un vecino al azar, revisa que no haya sido visitado
            -Destruye paredes entre la celda actual y la seleccionada
            -Añade la celda seleccionada al stack y continua
            -Si la celda nueva ya fue visitada, se hace backtracking
        Fin:
            -No existen celdas que no hayan sido visitadas

        "start" y "end" son tuplas que pueden especificar
        la posición de la entrada y la salida del laberinto.
        """

        # Actualiza 'start' y 'end' de acuerdo a los argumentos.
        # Define variables auxiliares.
        
        size = self.size
        bottom = size[0] -1
        right = size[1] -1
        if start == False:
            self.start = (0,0)
            start = self.start
        else: self.start = start
        if end == False:
            self.end = (bottom, right)
            end = self.end
        else: self.end = end

        # Elige una celda inicial al azar.
        cell = self.grid[random.randint(0,bottom)][random.randint(0,right)]
        cell.setVisited(True)
        stack = [cell]
        i = 0

        # Inicia el algoritmo de Recursive Backtracking
        while len(stack) > 0:

            try:
                newcell = self.chooseNew(cell)
                if newcell.getVisited():
                    cell = stack.pop()
                else:
                    cell.destroyWall(newcell)  
                    newcell.setVisited(True)
                    cell = newcell
                    stack.append(newcell)

            except :
                cell = stack.pop()

        # Agrega la entrada y la salida al laberinto.
        #implementación TRIVIAL!
        # self.grid[self.start[0]][self.start[1]].wallS = False
        #self.grid[self.end[0]][self.end[1]].wallN = False



    def chooseNew(self,cell):
        """
        Devuelve una celda vecina no visitada al azar.
        """
        options = cell.findNeighbours(self.grid, checkVisited=True)
        for i in options:
            if i.getVisited() != False:
                options.remove(i)
        if len(options) > 0: return random.choice(options)
        else: raise Exception("no unvisited neighbours")







#if __name__ == "__main__":
#    size = (10,25)
#    maze = BacktrackingMaze(size)
#   maze.buildMaze()
#    maze.saveMaze("testname")
