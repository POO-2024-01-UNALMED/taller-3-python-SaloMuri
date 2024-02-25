class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if 1 <= canal <= 120:
            self._canal = canal
        elif canal < 1:
            self._canal = 1
        elif canal > 120:
            self._canal = 120

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if 0 <= volumen <= 7:
            self._volumen = volumen
        elif volumen > 7:
            self._volumen = 7
        elif volumen < 0:
            self._volumen = 0

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numtv):
        cls._numTV = numtv

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False
        self._volumen = 0

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == True and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado == True and self._canal > 1:
            self._canal -= 1

    def volumenUp(self):
        if self._estado == True and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado == True and self._volumen > 0:
            self._volumen -= 1