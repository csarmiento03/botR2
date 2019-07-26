# Documentacion

## Simulación (main.py)

La simulación se ejecuta en el archivo **main.py**. Al principio se genera el laberinto y el bot que va a resolver el laberinto.

Se puede modificar el tamaño del laberinto a generar con la variable:

~~~
size = (Filas,Columnas)
~~~

En donde Filas y Columnas indican cuantas filas y columnas va a tener el laberinto respectivamente.

Luego hay un bucle en donde cada paso va a modificar la posición o la orientación de bot hasta que llegue al final del laberinto o pasen una cierta cantidad de pasos el cual indica que está perdido.

Cuando termina la simulación, se guardan los archivos del laberinto y del camino recorrido por el bot. Accediendo al archivo se puede indicar los nombres de los archivos a guardar.

## Visualización (usoVisualizador.py)

La simulación se ejecuta en el archivo **usoVisualizador.py** y requiere de los archivos generados en la simulación. En la visualización se pueden realizar 4 cosas diferentes:

* Generar imagen del laberinto vacio (Poner en True el flag *fotoLaberintoPelado*)
* Generar imagen del laberinto con una estela por donde anduvo el bot (Poner en True el flag *fotoBotEnAlgunLado*)
* Generar imagen del laberinto en algun instante cualquiera de cuando el bot anduvo recorriendolo (Poner en True el flag *fotoBotEnAlgunLado* e indicarle que cuadro con la variable numerica *frameBotEnAlgunLado* )
* Generar un video \*.mp4 (Poner en True el flag *video* e indicarle la tasa de cuadros por segundo con la variable *fps*)

En la visualización se posee multiples opciones de configuraciones, como definir que tipo de bot a usar (skin), cambiarle color, forma. Lo mismo para el laberinto, se puede cambiar el color y el estilo de dibujo. En el video, ademas de definir los cuadros por segundo, se puede definir con que suavidad sea el movimiento del bot cuando avanza celda a celda. Con la variable *smoothFrames* se puede definir cuanto cuadros se intercalaran ente el movimiento de celda a celda. Si es igual a 5, habra 5 cuadros entre movimiento  de celda a celda, 3, habra 3 cuadros entre movimiento de celda a celda, etc.

Los archivos se guardan con el nombre definido en *mediaFilename* y se le agrega un sufijo para cada tipo de visualización. Por ejemplo:

~~~
lab5x15_003.mp4 : Video
lab5x15_003_maze.png : Imagen del laberinto vacio
lab5x15_003_resolution.png : Imagen del laberinto con la estela del bot
lab5x15_003_frame5.png : Imagen del laberinto con el bot adentro en el cuadro 5
~~~

## Archivos de comunicación

En esta sección se explica como es el formato de los archivos de comunicación entre la simulación. Todos los archivos son **csv** por lo que son accesible por el usuario y no depende de ninguna plataforma particular para funcionar.

### Archivo que guarda el laberinto:

Se recomiendan que tenga extensión .maze. Se da un ejemplo del contenido de un laberinto de 6x6:

~~~
19,6,3,10,10,6
13,5,5,3,10,12
7,9,12,5,3,6
1,2,14,5,5,5
5,13,3,12,5,5
9,10,8,10,12,45
~~~

Como se vé, es una matriz de *n x m*. Cada elemento de la matriz representa una de las celdas del laberinto. La forma del laberinto está dada por la cantidad de filas y columnas que posee.

En cada celda está codificado en binario que paredes posee y si son la entrada o la salida del laberinto. Por ejemplo se tiene el numero 6, en binario sería:

~~~
0b0110
~~~

Cada posicion de las primeranumeross 4 de ese número en binario reprenta una de las paredes, empezando de la pared del *oeste* en la 1ra posición, *norte* la 2da posición, *este* la 3ra y *sur* la cuarta.

![Numeracion pared Celda](https://github.com/csarmiento03/botR2/blob/master/docimage1.png)

Por lo que, teniendo eso en cuenta, el número binario

~~~
0b0110
~~~

Significa que esa celda tiene una pared en el *norte* y una en el *este*.

Por otro lado, si se pone un uno en la quinta posición del numero binario, significa que es una entrada. Por ejemplo:

~~~
19 = 0b010011
~~~

Y si se pone un uno en la sexta posición del numero binario, significa que es una salida. Por ejemplo:

~~~
45 = 0b101101
~~~

Si se desea crear un archivo con un laberinto respetando este formato es muy sencillo:

~~~
Celda =  2^3 * ParedSur  + 2^2 * ParedEste + 2^1 * ParedNorte  + 2^0 * ParedOeste

CeldaEntrada = 2^4 * Entrada + Celda
CeldaSalida = 2^5 * Salida + Celda
~~~

En donde :
* ParedSur, ParedEste, ParedNorte, ParedOeste: Valen 1 si hay una pared en esa parte o 0 si no.
* Entrada: Vale 1 si hay esa celda es una entrada o 0 si no.
* Salida: Vale 1 si hay esa celda es una salida o 0 si no.

Para la poder recuperar la información, se debe analizar el número binario cada posición si es un 1 o un 0 y con eso usarse para reconstruir el laberinto.

### Archivo que guarda el recorrido del bot:

Se recomiendan que tenga extensión .traj. Se da un ejemplo:

~~~
0, 0, 1
1, 0, 2
0, 0, 0
0, 1, 3
1, 1, 2
2, 1, 2
2, 2, 3
1, 2, 0
0, 2, 0
...
~~~

Cada fila del archivo es un paso que realizo el bot en el laberinto. En cada fila se observan 3 elementos:

~~~
0, 0, 1
x  y  Orientación
~~~

Los primeros dos elementos es la coordenada del bot (que representa una de las celdas del laberinto). El tercer elemento codifica la orientación del bot, en donde 0 significa mirando hacia el Norte, 1 hacia el Oeste, 2 hacia el Sur y 3 hacia el Este.
