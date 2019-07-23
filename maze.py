import numpy as np
import random
# import cell

class Cell():
	"""
	Clase mínima para testeo!
	"""
	def __init__(self,pos):
		self.pos = pos

	def __str__(self):
		return str(self.pos)

class Maze():
	"""
	Esta versión genérica solo construlle un laberinto trivial 
	que consiste en una caja con una entrada y una salida.

	"""

	def __init__(self):
		self.grid = None


	def buildMaze(self, size, start=False, end=False):
		"""
		Construye una grilla que representa al laberinto.
		sus argumentos de entrada son size, una tupla (Filas,Columnas)
		start y end, tuplas con las coordenadas de entrada y salida del
		laberinto.
		"""
		# Asigna inicio y final por default
		if not start: start = (0,0)
		if not end: end = size

		# Creal la grid y la inicializa con celdas
		self.grid = list()
		for i in range(size[0]):
			row = list()
			for j in range(size[1]):
				row.append(Cell(pos=(i,j)))
			self.grid.append(row)

		for row in self.grid:
			for cell in row:
				print(cell)	


if __name__ == "__main__":
	maze = Maze()
	maze.buildMaze((4,4))
