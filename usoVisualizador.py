import vis as vis

# Configuraciones
mediaFilename="resolucion2"  #Nombre que va a guardar los archivos

fotoLaberintoPelado = True  #Habilita el guardado de la foto del laberinto pelado
fotoCaminoBot = True        #Habilita el guardado de la foto del laberinto con el camino del bot
fotoBotEnAlgunLado = True   #Habilita el guardado de la foto del laberinto con el bot en algun punto
frameBotEnAlgunLado = 0     #Cuadro que se quiere sacar foto
video = True                #Habilita el guardado del video
fps=10                      #Cuadros por segundos para el video

robot = True
archMaze = "lab10.txt"      #Archivo de laberinto
archBot = "botpath.txt"     #Archivo de camino de bot

cellSize = 2                #Tamaño de las celdas del laberinto
xkcd = True                 #Habilita forma xkcd
colorWall="k"               #Color de las paredes del laberintos
entryColor="palegreen"      #Color de la entrada
exitColor="lightcoral"      #Color de la salida

numVerticesBot=3            #De cuantos vertices es el bot
faceColorBot="m"            #De que color es el bot
smoothFrames=5              #Cuantos cuadros de suavizado se desea generar

#Cargamos el laberinto
laberinto = vis.MazeForVisualization()
laberinto.loadMazeFile(archMaze)

#Creamos el bot
if robot:
    bot = vis.RegularPolygonBot(numVertices=numVerticesBot, faceColor=faceColorBot)
    bot.loadPath(archBot)
    bot.smoothingPath(frames=smoothFrames)

    vv = vis.Visualizer(laberinto, bot, cellSize, mediaFilename=mediaFilename)
else:
    vv = vis.Visualizer(laberinto, None, cellSize, mediaFilename=mediaFilename)

if fotoLaberintoPelado:
    vv.showMaze(xkcd=xkcd, colorWall=colorWall, entryColor=entryColor ,exitColor=exitColor)

if fotoCaminoBot:
    vv.showMazeWithResolution(xkcd=xkcd, colorWall=colorWall, entryColor=entryColor ,exitColor=exitColor)

if fotoBotEnAlgunLado:
    vv.showMazeWithBot(frame=frameBotEnAlgunLado, xkcd=xkcd, colorWall=colorWall, entryColor=entryColor ,exitColor=exitColor)

if video:
    mazeTuple=(xkcd, colorWall, entryColor, exitColor)
    vv.animator(mazeTuple, fps)
