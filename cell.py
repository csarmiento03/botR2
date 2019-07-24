#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  cell.py


class Cell(object):

    """
    Clase que conforma laberintos con atributos y métodos que facilitan su construcción.
    Atributos:
        pos: una tupla de enteros del tipo (y,x) ó (row, col).
        start: una tupla de enteros del tipo (y,x) ó (row, col).
        end: una tupla de enteros del tipo (y,x) ó (row, col).
        visited: bool
        wall{W,N,E,S}: bool que representa las paredes en dirección de puntos cardinales.
    """

    def __init__(self, pos, walls=False):
        self.pos = pos         
        self.start = False
        self.end = False
        self.visited = False
        if walls:
            self.wallW = True
            self.wallN = True
            self.wallE = True
            self.wallS = True
        else:
            self.wallW = False
            self.wallN = False
            self.wallE = False
            self.wallS = False

    """ 
    Conjunto de setters y getters para respetar el paradigma OOP.
    """
    def setStart(self, arg):
        """
        Asigna 'arg' a 'start'
        """
        self.start = arg

    def getStart():
        """
        Devuelve 'start'
        """
        return self.start

    def setEnd(self, arg):
        """
        Asigna 'arg' a 'end'
        """
        self.end = arg

    def getEnd(self):
        """
        Devuelve 'end'
        """
        return self.end

    def setVisited(self, arg):
        """
         Asigna 'arg' a 'visited'
        """
        self.visited = arg

    def getVisited(self):
        """
        Devuelve 'visited'
        """
        return self.visited

    def getWalls(self):
        """
        Devuelve una lista de {0,1} indicando la existencia de paredes.
        El orden de los elementos es [W,N,E,S].
        """
        return [int(self.wallW), int(self.wallN),
                int(self.wallE), int(self.wallS)]
        
    def getPos(self):
        """
        devuelve 'pos'
        """
        return self.pos

    def sumWalls(self):
        """
        Computa un codigo específico para la representación 2D de la celda en el laberinto.
        El código se encuentra especificado en 'doc.md'.
        """
        total = int(self.wallW) + 2*int(self.wallN) 
        total += 4*int(self.wallE) + 8*int(self.wallS)
        return total

    def findNeighbours(self, grid, checkVisited=True):
        """
        Devuelve una lista de celdas vecinas.
        grid: atributo de maze.
        checkVisited: [optional] devuelve solo las celdas vecinas que
                      no hayan sido visitadas hasta el momento.
        """    

        neighbours = []
        # Define los indices de los posibles vecinos e intenta indexarlos.
        tries = [(self.pos[0]+1, self.pos[1]), (self.pos[0]-1, self.pos[1]),
                (self.pos[0], self.pos[1]+1), (self.pos[0], self.pos[1]-1)]
        for t in tries:
            if t[0] >= 0 and t[1] >= 0:
                try: neighbours.append(grid[t[0]][t[1]])
                except: pass

        # Desindexa los vecinos que ya han sido visitados.
        if checkVisited:
            for i in neighbours:
                if i.getVisited() != False:
                    neighbours.remove(i)
        return neighbours
 
    def checkWall(self, otherCell):
        """
        Revisa si existe una pared que conecte con 'otherCell' y devuelve un bool.
        otherCell: objeto 'Cell' que se encuentra contiguo en la 'grid' de un 'Maze'
        """   
        x0 = self.pos[1]
        y0 = self.pos[0]
        x1 = otherCell.pos[1]
        y1 = otherCell.pos[0]
        dx = x0-x1
        dy = y0-y1
        if dx == 0 and dy == 1 and self.wallN:
            return True
        elif dx == 0 and dy == -1 and self.wallS:
            return True
        elif dx == -1 and dy == 0 and self.wallE:
            return True
        elif dx == 1 and dy == 0 and self.wallW:
            return True
        else:
            return False

    def destroyWall(self,otherCell):
        """
        Destruye las paredes que conectan con 'otherCell'
        otherCell: objeto 'Cell' que se encuentra contiguo en la 'grid' de un 'Maze'
        """
        x0 = self.pos[1]
        y0 = self.pos[0]
        x1 = otherCell.pos[1]
        y1 = otherCell.pos[0]
        dx = x0-x1
        dy = y0-y1
        if dx == 0 and dy == 1:
            self.wallN = False
            otherCell.wallS = False
        elif dx == 0 and dy == -1:
            self.wallS = False
            otherCell.wallN = False
        elif dx == -1 and dy == 0:
            self.wallE = False
            otherCell.wallW = False
        elif dx == 1 and dy == 0:
            self.wallW = False
            otherCell.wallE = False            
        else:
            print("No se pudo romper!!!")
        
        
        
        
        
