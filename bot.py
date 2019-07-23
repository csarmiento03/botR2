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

        """Cambia la orientacion del robot hacia la direccion indicada con el 
        indice i"""

        if self.sensor[np.nonzero(self.orientation)] == 0:
            pass
        else:
            if np.nonzero(self.orientation) == 0:
                if self.sensor[1] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[1] = 1
                elif self.sensor[3] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[3] = 1
                else:
                    self.orientation = np.zeros(4)
                    self.orientation[2] = 1
            elif np.nonzero(self.orientation) == 1:
                if self.sensor[2] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[2] = 1
                elif self.sensor[0] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[0] = 1
                else:
                    self.orientation = np.zeros(4)
                    self.orientation[3] = 1
            elif np.nonzero(self.orientation) == 2:
                if self.sensor[3] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[3] = 1
                elif self.sensor[1] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[1] = 1
                else:
                    self.orientation = np.zeros(4)
                    self.orientation[0] = 1
            else:
                if self.sensor[0] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[0] = 1
                elif self.sensor[2] == 0:
                    self.orientation = np.zeros(4)
                    self.orientation[2] = 1
                else:
                    self.orientation = np.zeros(4)
                    self.orientation[1] = 1
        
                    
