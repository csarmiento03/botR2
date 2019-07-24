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
        self.start = None
        self.end = None
        self.orphans = []
        self.trajectory = []

    def getWalls(self, pos)
        return self.grid[pos[0]][pos[1]].getWalls()

    def saveMaze(self, fname):
        size = (len(self.grid), len(self.grid[0]))
        data = np.zeros(size, dtype=int)
        for row in range(size[0]):
            for col in range(size[1]):
                data[row,col] = int(self.grid[row][col].sumWalls())
        data[self.start[0], self.start[1]] += 16
        data[self.end[0],self.end[1]] += 32
        # for o in self.orphans:
        #     data[o.pos[0], o.pos[1]] += 64
        np.save(fname, data)
        tfile = open(fname+".traj", "w")
        for t in self.trajectory:
            tfile.writelines("{},\t{}\n".format(t[0], t[1]))
        tfile.close()


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
        self.start = start
        self.end = end

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

        # Inicializa 'start' y 'end' por default. Define variables auxiliares
        bottom = size[0] -1
        right = size[1] -1
        if not start: start = (0,0)
        if not end: end = (bottom, right)
        self.start = start
        self.end = end

        stack = []
        cell = self.grid[random.randint(0,bottom)][random.randint(0,right)]
        cell.setVisited(True)
        stack.append(cell)
        i = 0
        while len(stack) > 0:
            traj = (cell.pos, [c.pos for c in cell.findNeighbours(self.grid)])
            self.trajectory.append(traj)
            print("step:\t{}\tstackLen:\t{}\tpos:\t{}".format(i,len(stack),stack[-1].pos))
            i += 1
            newcell = self.chooseNew(cell)
            if not newcell.getVisited():
                stack.append(newcell)
                newcell.setVisited(True)
                cell.destroyWall(newcell)
                cell = newcell
                continue
            else: 
                cell = stack.pop()


        for row in self.grid:
            for cell in row:
                if cell.getVisited() == False:
                    self.orphans.append(cell)
        print("orphans:")
        print([c.pos for c in self.orphans])



    def chooseNew(self,cell):
        """
        Elige una nueva celda vecina al azar y la devuelve.
        """
        return random.choice(cell.findNeighbours(self.grid, checkVisited=True))
        






if __name__ == "__main__":
    maze = BacktrackingMaze()
    # maze = BoxMaze()
    size = (5,5)
    maze.initMaze(size)
    maze.buildMaze(size)
    maze.saveMaze("testname")
