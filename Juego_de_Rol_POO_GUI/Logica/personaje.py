from abc import ABC, abstractmethod
from Logica.raza import Raza
from Logica.Manejador_de_Exceptions import *

class Personaje(ABC):
    def __init__(
        self, nombre = "Desconocido", 
        raza = Raza.NINGUNA, 
        fuerza = 0, 
        inteligencia = 0, 
        vida_maxima = 100):
        
        self.nombre = nombre
        self.raza = raza
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, value):
        self._raza = value

    @property
    def fuerza(self):
        return self._fuerza

    @fuerza.setter
    def fuerza(self, value):
        self._fuerza = value

    @property
    def inteligencia(self):
        return self._inteligencia

    @inteligencia.setter
    def inteligencia(self, value):
        self._inteligencia = value

    @property
    def vida_actual(self):
        return self._vida_actual

    @vida_actual.setter
    def vida_actual(self, value):
        if ((value < 0) or (value > 100)):
            raise PuntosDeVidaException("La vida del personaje debe estar en un intervalo de 0-100")
        else:
            self._vida_actual = value
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.raza}, {self.fuerza}, {self.inteligencia}, {self.vida_actual}"

