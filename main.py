import numpy as np
import bot as b
import maze as mz

#=======================================================================================
#                                Funciones
#=======================================================================================
                       
def orientation2int(orientation):
    """
    Convierte el vector 'bot.orientation' en un entero codificado.
    El código está explicado en 'doc.md'.
    """
    index = int(np.nonzero(orientation)[0])
    if index == 0: return 1
    elif index == 1: return 0
    elif index == 2: return 3
    elif index == 3: return 2
    else: raise Exception()

def saveTrajectory(traj, fname):
    """
    Guarda la trayectoria de un robot almacenada en 'traj' en un archivo 'fname'.
    El formato de archivo está explicado en 'doc.md'.
    """
    tfile = open(fname, "w")
    line = "{}, {}, {}\n"
    for step in traj:
        fields = [step[0], step[1], orientation2int(step[2])]
        tfile.writelines(line.format(*fields))
    tfile.close()

#=======================================================================================
#         Inicialización de variables y objetos necesarios para la simulación.
#=======================================================================================       


#--------------------Creación del Laberinto y variables--------------------------------- 

size = (20,20)                                       
maze = mz.BacktrackingMaze(size)
maze.buildMaze()
maze.saveMaze("laberinto")

mazeEnd = np.array(maze.getEnd())

#-----------------Creación del Robot y variables----------------------------------------

bb8 = b.Bot()

traj = []         #Trayectoria del Robot


botPosition = np.array(maze.getStart())
botOrientation = bb8.getOrientation()


#=======================================================================================
#                               Resolución             
#=======================================================================================

solved = False

steps = 0

while solved == False:


    traj.append((botPosition[0], botPosition[1], botOrientation))

    bb8.detect(maze.getWalls(botPosition))
    
    bb8.decide2()

    botOrientation = bb8.getOrientation()    

    aux = np.nonzero(botOrientation)[0][0]


#   Actualización de la posición del robot

 
    if aux == 0:
        
        botPosition[1] -= 1
    
    elif aux == 1:

        botPosition[0] -= 1

    elif aux == 2:

        botPosition[1] += 1

    elif aux == 3:

        botPosition[0] += 1


#   Condiciones de éxito y fracaso 
    
    steps += 1

    
    if botPosition[0] == mazeEnd[0] and botPosition[1] == mazeEnd[1]:

        solved = True
        
        print("El robot ha salido del laberinto exitosamente !! :D")

    if steps>=10000:

        print("Me perdí !! Estoy perdido en la facultad de químicas")
        
        break


print("Hice",steps,"pasos")


traj.append((botPosition[0], botPosition[1], botOrientation))

saveTrajectory(traj, "bb8.traj")












































