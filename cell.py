#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  cell.py


class Cell(object):
    """Definicion del constructor de la clase donde escribo todos los 
    atributos o variables que va a tener la clase y que pueden 
    ser llamados por los otros objeto"""
    def __init__(self, pos, walls):
        self.pos = pos         
        self.star = True
        self.end = True
        self.visited = False
        self.wallN = True
        self.wallS = True
        self.wallE = True
        self.wallW = True
    
    """setter y getter para iniciar y finzalizar la construcción del
    laberinto."""
    def setStart(self, arg):
        self.start = arg
    def getStar():
        return self.star()
        
    def setEnd(self, arg):
        self.end = arg
    def getEnd():
        return self.end()
    
    def getWalls(self):
        pass
        
    def setVisited(self, arg):
        self.visited =arg
    def getVisited(self, arg):
        return self.visited()
    
    """Metodo encontrar vecinos en el cual, primero se calculan 
    los primeros vecinos respecto a su posicion actual. Luego, se
    revisa si esos vecinos hacen parte de la grilla y si han sido
    o no visitados. Para esto, se usa el atributo visited"""    
    def findNeighbours(self, grid):
        
        auxList = []
        try: auxList.append(grid[self.pos[0]+1][self.pos[1]])
        except: pass
        try: auxList.append(grid[self.pos[0]-1][self.pos[1]])
        except: pass
        try: auxList.append(grid[self.pos[1]+1][self.pos[0]])
        except: pass
        try: auxList.append(grid[self.pos[1]-1][self.pos[0]])
        except: pass

        for i in auxList:
            if i.visited == True:
                auxList.pop(i)
    """Metodo que hace una revision de la ubicacion de la otra
    celda con respecto a la celda en la cual se encuentra.
    """    
    def checkWall(self, otherCell):
        x0 = self.pos[1]
        y0 = self.pos[0]
        x1 = otherCell.pos[1]
        x1 = otherCell.pos[0]
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
    """Metodo para destruir la pared de la celda vecina.
    Aquí rompe su propia pared y la del otro.
    """
    def destroyWall():
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
        
        
        
        
        
