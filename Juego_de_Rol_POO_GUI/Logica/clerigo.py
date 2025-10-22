from Logica.personaje import Personaje
from Logica.raza import Raza
from Logica.Manejador_de_Exceptions import *

class Clerigo(Personaje):
        def __init__(
        self, nombre = "Desconocido", 
        raza = Raza.NINGUNA, 
        fuerza = 9, 
        inteligencia = 4, 
        vida_maxima = 100, 
        nombre_Dios = "Dios"):
            super().__init__(nombre, raza, fuerza, inteligencia, vida_maxima)
            self.__don_Curacion = False
            self.__nombre_Dios = nombre_Dios

        @property
        def _don_Curacion(self):
            return self.__don_Curacion

        @_don_Curacion.setter
        def _don_Curacion(self, value):
            self.__don_Curacion = value

        @property
        def _nombre_Dios(self):
            return self.__nombre_Dios

        @_nombre_Dios.setter
        def _nombre_Dios(self, value):
            self.__nombre_Dios = value

            
        def rezar(self):
            if (self._don_Curacion == False):
                self._don_Curacion = True
                return f"El Clerigo {self.nombre} ha rezado a {self._nombre_Dios} y se le ha otorgado el don de la curación"
            else:
                return "EL Clerigo ya posee el don de la curación"
        
        def curar(self, personaje : Personaje):
            if (self._don_Curacion == True):
                
                try:
                    personaje.vida_actual = personaje.vida_actual + 10
                    self.don_Curacion = False
                    return f"El Clerigo {self.nombre} ha curado a el {personaje.__class__.__name__} {personaje.nombre} con 10 puntos mas de vida"
                except PuntosDeVidaException as e:
                    return e.mensaje      
            else:
                return "El Clerigo debe rezar primero para obtener el don de la curación"