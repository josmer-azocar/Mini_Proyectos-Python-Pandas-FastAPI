class PuntosDeVidaException(Exception):
    def __init__(self, mensaje="Error relacionado a la Vida del personaje"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)