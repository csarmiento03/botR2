import numpy as np

class Bot(object):
    """Clase base de robot"""

    def __init__(self):

        """constructor de la clase Bot """
        
        """El sensor guarda la ultima deteccion del entorno del robot, cuyo
         formato es un array de np de dim. 4, donde cada elemento corresponde 
        a una pared
        La orientacion indica hacia donde esta apuntando el robot. La posicion 
        a la que apunta es indicada con un cero. Inicialmente
        apunta hacia el oeste"""
        
        self.sensor = np.zeros(4)
        self.orientation = np.array([1,0,0,0])

    def detect(self,walls):
 
        """El robot detecta las cuatro paredes alrededor suyo:
        el primer elemento corresponde a la pared Oeste, el segundo a 
        la pared Norte, el tercero a la pared Este y el ultimo a la Sur."""
	
        self.sensor = walls

    def decide(self):

        """Cambia la orientacion del robot segun lo que indique su sensor.
        Siempre quedara apuntando a una direccion en la que no haya una pared.
        Primero verificara si delante suyo hay pared. Si no hay, se quedara 
        en esa posicion. Luego, intentara hacia su derecha, luego a su izquierda
        y por ultimo hacia atras."""

        aux = np.nonzero(self.orientation)[0][0]

        if self.sensor[aux] == 0:
            pass
        else:
            if self.sensor[aux-3] == 0:
                
                self.orientation = np.zeros(4)
                self.orientation[aux-3] = 1
                
            elif self.sensor[aux-1] == 0:
                
                self.orientation = np.zeros(4)
                self.orientation[aux-1] = 1
            elif self.sensor[aux-2] == 0:
                
                self.orientation = np.zeros(4)
                self.orientation[aux-2] = 1
                
    def getOrientation(self):
        
        """Metodo para obtener el atributo orientation"""
        
        return self.orientation
