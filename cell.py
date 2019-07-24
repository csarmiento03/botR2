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
        return self.start()
	    
    def setEnd(self, arg):
        self.end = arg

    def getEnd():
        return self.end()

    def setVisited(self, arg):
        self.visited = arg

    def getVisited(self, arg):
        return self.visited()

    def getWalls(self):
        return [self.wallW, self.wallN, self.wallE, self.wallS]
        
    def findNeighbours(self, grid):
        """
        Metodo encontrar vecinos en el cual, primero se calculan 
        los primeros vecinos respecto a su posicion actual. Luego, se
        revisa si esos vecinos hacen parte de la grilla y si han sido
        o no visitados. Para esto, se usa el atributo visited.
        """    

        # neighbours = []
        # try: neighbours.append(grid[self.pos[0]+1][self.pos[1]])
        # except: pass
        # try: neighbours.append(grid[self.pos[0]-1][self.pos[1]])
        # except: pass
        # try: neighbours.append(grid[self.pos[1]+1][self.pos[0]])
        # except: pass
        # try: neighbours.append(grid[self.pos[1]-1][self.pos[0]])
        # except: pass

        # Lo de arriba, pero reimplementado en menos lineas y corregido error en los índices!
        tries = [(self.pos[0]+1, self.pos[1]), (self.pos[0]-1, self.pos[1]),
                (self.pos[0], self.pos[1]+1), (self.pos[0], self.pos[1]-1)]
        for t in tries:
            try: neighbours.append(grid[t[0]][t[1]])
            except: pass

        for i in neighbours:
            if i.visited:
                neighbours.pop(i)
 
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
        if dx==1 and dy==0 and wallN:
            return True
        elif dx==-1 and dy==0 and wallS:
            return True
        elif dx==0 and dy==-1 and wallE:
            return True
        elif dx==0 and dy==1 and wallW:
            return True
        else:
            return False

    def destroyWall():
        """
        Metodo para destruir la pared de la celda vecina.
        Aquí rompe su propia pared y la del otro.
        """
        x0 = self.pos[1]
        y0 = self.pos[0]
        x1 = otherCell.pos[1]
        x1 = otherCell.pos[0]
        dx = x0-x1
        dy = y0-y1
        if dx==1 and dy==0:
            self.wallN = False
            otherCell.wallS = False
        elif dx==-1 and dy==0:
            self.wallS = False
            otherCell.wallN = False
        elif dx==0 and dy==-1:
            self.wallE = False
            otherCell.wallW = False
        elif dx==0 and dy==1:
            self.wallW = False
            otherCell.wallE = False            
        else:
            print("No se pudo romper!!!")
        
        
        
        
        
