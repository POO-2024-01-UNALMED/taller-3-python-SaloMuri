class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def setNombre(self, nombreMarca):
        self._nombre = nombreMarca

    def getNombre(self):
        return self._nombre