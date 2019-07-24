import numpy as np
import bot as b
from maze import Maze

maze = BacktrackingMaze()

size = (4,4)

maze.initMaze(size)
mazebuildMaze(size)
maze.saveMaze("Prueba 1")

bb8 = b.Bot()

mazeEnd = maze.getEnd()
botPosition = maze.getStart()
botOrientation = bb8.getOrientation()

botInformation = [botPosition,botOrientation]   

solved = False


f = open("Bb8.traj","w+") 

np.savetxt( "Bb8.traj" , botInformation)

steps = 0

#---------------------------------------------------------------
while solved == False:


    bb8.detect(maze.getWalls(botPosition))
    
    bb8.decide()

    botOrientation = bb8.getOrientation()    

    aux = np.nonzero(botOrientation)[0][0]
#   ---------------------------------------------
    if aux == 0:
        
        botPosition[1] -= 1
    
    elif aux == 1:

        botPosition[0] -= 1

    elif aux == 2:

        botPosition[1] += 1

    elif aux == 3:

        botPosition[0] += 1
#   ----------------------------------------------    
    
    botInformation = [botPosition,botOrientation]  
    
    
    np.savetxt( "Bb8.traj" , botInformation)

    steps += 1

    if botPosition == mazeEnd:

        solved = True
        
        print("El robot ha salido del laberinto exitosamente !! :D")

    if steps>100:

        break
        
        print("Me perdí !! Estoy perdido, estoy en la facultad de químicas")

#---------------------------------------------------------------------

f.close()

























