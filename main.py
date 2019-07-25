import numpy as np
import bot as b
import maze as mz

size = (4,4)

maze = mz.BacktrackingMaze(size)
maze.buildMaze()
maze.saveMaze("laberinto")

bb8 = b.Bot()

mazeEnd = np.array(maze.getEnd())
botPosition = np.array(maze.getStart())
botOrientation = bb8.getOrientation()

botInformation = [botPosition,botOrientation]   

solved = False


f = open("Bb8.traj","w+") 

#np.save( "Bb8.traj" ,botPosition[0])

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
    
    
    #np.savetxt( "Bb8.traj" , botPosition[0])
    
    steps += 1

    print(botPosition)
    
    if botPosition[0] == mazeEnd[0] and botPosition[1] == mazeEnd[1]:

        solved = True
        
        print("El robot ha salido del laberinto exitosamente !! :D")

    if steps>=100:

        print("Me perdí !! Estoy perdido, estoy en la facultad de químicas")
        
        break

print("Hice",steps,"pasos")
#---------------------------------------------------------------------

f.close()















