class Hechizo:
    def __init__(self, nombre = "Hechizo simple", efecto = 0):
        self.__nombre = nombre
        self.__efecto = efecto

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _efecto(self):
        return self.__efecto

    @_efecto.setter
    def _efecto(self, value):
        self.__efecto = value


