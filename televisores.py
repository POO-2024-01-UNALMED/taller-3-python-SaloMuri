class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def setNombre(self, nombreMarca):
        self._nombre = nombreMarca

    def getNombre(self):
        return self._nombre
    

class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        self._canal = canal

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
    
    @classmethod
    def getNumTV(cls):
        cls.numTV += 1
        return cls.numTV
    
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1:
            self._canal -= 1

    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0:
            self._volumen -= 1


class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, televisor):
        self._tv = televisor
        televisor.setControl(self)

    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        if self._tv:
            self._tv.setVolumen(volumen)

    def setTv(self, televisor):
        self._tv = televisor

    def getTv(self):
        return self._tv