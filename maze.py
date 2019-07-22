import numpy as np
import random

class Maze():
	# def __init__():

	def buildMaze(self, size, start=False, end=False):
		"""
		Construye una grilla que representa al laberinto.
		sus argumentos de entrada son size, una tupla (Filas,Columnas)
		start y end, tuplas con las coordenadas de entrada y salida del
		laberinto

		"""
		maze = np.ones(size)
		#Define posición inicial y final
		if not start: start = (0,0)
		if not end: end = (size[0], size[1]) #esto no se si aplica
		maze[0,0,0] = 0
		maze[0,1,0] = 0
		print(maze)

if __name__ == "__main__":
	maze = Maze()
	maze.buildMaze((4,4))
	maze