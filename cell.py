#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  cell.py


class Cell(object):

    """
    Clase que conforma laberintos con atributos y métodos que facilitan su construcción.
    """

    def __init__(self, pos, walls=False):
        """
        Definicion del constructor de la clase donde escribo todos los 
        atributos o variables que va a tener la clase y que pueden 
        ser llamados por los otros objeto.
        """
        self.pos = pos         
        self.start = False
        self.end = False
        self.visited = False
        if walls:
            self.wallN = True
            self.wallS = True
            self.wallE = True
            self.wallW = True
        else:
            self.wallN = False
            self.wallS = False
            self.wallE = False
            self.wallW = False

    """ Setters y getters para respetar el paradigma OOP."""
    def setStart(self, arg):
        self.start = arg

    def getStart():
        return self.start

    def setEnd(self, arg):
        self.end = arg

    def getEnd(self):
        return self.end

    def setVisited(self, arg):
        self.visited = arg

    def getVisited(self):
        return self.visited

    def getWalls(self):
        return [int(self.wallW), int(self.wallN),
                int(self.wallE), int(self.wallS)]
        
    def getPos(self):
        return self.pos

    def sumWalls(self):
        total = int(self.wallW) + 2*int(self.wallN) 
        total += 4*int(self.wallE) + 8*int(self.wallS)
        return total

    def findNeighbours(self, grid, checkVisited=True):
        """
        Metodo encontrar vecinos en el cual, primero se calculan 
        los primeros vecinos respecto a su posicion actual. Luego, se
        revisa si esos vecinos hacen parte de la grilla y si han sido
        o no visitados. Para esto, se usa el atributo visited.
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
                if i.getVisited(): neighbours.remove(i)
        print([n.pos for n in neighbours])
        return neighbours
 
    def checkWall(self, otherCell):
        """
        Metodo que hace una revision de la ubicacion de la otra
        celda con respecto a la celda en la cual se encuentra.
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
        Metodo para destruir la pared de la celda vecina.
        Aquí rompe su propia pared y la del otro.
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
        
        
        
        
        
