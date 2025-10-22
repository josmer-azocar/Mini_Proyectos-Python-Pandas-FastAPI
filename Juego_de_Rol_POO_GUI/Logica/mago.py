from Logica.personaje import Personaje
from Logica.raza import Raza
from Logica.hechizo import Hechizo

class Mago(Personaje):
    def __init__(
        self, nombre = "Desconocido", 
        raza = Raza.NINGUNA, 
        fuerza = 3, 
        inteligencia = 7, 
        vida_maxima = 100):
        super().__init__(nombre, raza, fuerza, inteligencia, vida_maxima)
        self.__Hechizos = []     

    @property
    def _Hechizos(self):
        return self.__Hechizos

    @_Hechizos.setter
    def _Hechizos(self, value):
        self.__Hechizos = value

    def aprenderHechizo(self, hechizo: Hechizo):
        for elemento in self.__Hechizos:
            if elemento.nombre == hechizo._nombre: 
                return "El Mago ya conoce ese Hechizo"
            
        if len(self.__Hechizos) < 5:
            self.__Hechizos.append(hechizo)
            return f"EL Mago {self.nombre} ha aprendido --{hechizo._nombre}-- exitosamente"
        else:
            return "El Mago no puede aprender mas Hechizos"

    def olvidarHechizo(self, nombre_hechizo):
        for elemento in self.__Hechizos:
            if (elemento._nombre == nombre_hechizo):
                self.__Hechizos.remove(elemento)
                return f"El Mago {self.nombre} ha olvidado el Hechizo --{nombre_hechizo}-- correctamente"
            
        return "El Mago no conoce ese Hechizo"

    def lanzarHechizo(self, personaje : Personaje, nombre_hechizo):
        for elemento in self.__Hechizos:
            if (elemento._nombre == nombre_hechizo):
                personaje.vida_actual = personaje.vida_actual - elemento._efecto
                return f"El {personaje.__class__.__name__} {personaje.nombre} ha perdido {elemento._efecto} puntos de vida"
        
        return "El hechizo que intenta lanzar no existe"