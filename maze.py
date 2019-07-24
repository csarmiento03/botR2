#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  maze.py

import numpy as np
import random
from cell import Cell



class Maze():
    """
    Esta versión genérica solo construlle un laberinto trivial 
    que consiste en una caja con una entrada y una salida.

    """

    def __init__(self):
        self.grid = None

    def saveMaze(self, fname):
        pass

    def initMaze(self, size, walls=True):
        """
        Crea la grid de dimensiones dadas por "size".
        "walls" indica si las celdas están rodeadas de paredes por defecto.
        """
        self.grid = list()
        for i in range(size[0]):
            row = list()
            for j in range(size[1]):
                row.append(Cell(pos=(i,j), walls=walls))
            self.grid.append(row)

    def buildMaze(self,size, start=False, end=False):
        """
        Función dummy
        """
        pass

class BoxMaze(Maze):

    def buildMaze(self, size, start=False, end=False):
        """
        Crea un laberinto trivial de tamaño "size" que consiste en
        una caja vacía. "start" y "end" son tuplas que pueden especificar
        la posición de la entrada y la salida del laberinto.
        """
        # Asigna entrada y salida por default. Define variables auxiliares.
        bottom = size[0] -1
        right = size[1] -1
        if not start: start = (0,0)
        if not end: end = (bottom, right)


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

        #Implementa la entrada y salida.
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

    def buildMaze(self,size,start=False,end=False):
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
        stack = []
        cell = grid[random.randint(0,bottom)][random.randint[0,right]]
        cell.setVisited(True)
        stack.append(cell)
        while len(stack) > 0:
            try: 
                newcell = chooseNew(self,cell)
                if not newcell.getVisited():
                    cell.destroyWall(newcell)
                    newcell.setVisited(True)
                    stack.append(newcell)
                    continue
                else: 
                    cell = stack.pop()
            except: pass

    def chooseNew(self,cell):
        """
        Elige una nueva celda vecina al azar y la devuelve.
        """
        pass






if __name__ == "__main__":
    maze = BoxMaze()
    size = (3,3)
    maze.initMaze(size)
    maze.buildMaze(size)
