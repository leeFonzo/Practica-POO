class Movimiento:
    __nCuenta:int
    __fecha:str
    __desc:str
    __tipo:str
    __importe:float
    def __init__(self, nCuenta, fecha, desc, tipo, importe):
        self.__nCuenta=nCuenta
        self.__fecha=fecha
        self.__desc=desc
        self.__tipo=tipo
        self.__importe=importe

    def getNumCuenta(self):
        return self.__nCuenta
    def getFecha(self):
        return self.__fecha
    def getDescripcion(self):
        return self.__desc
    def getTipo(self):
        return self.__tipo
    def getImporte(self):
        return self.__importe        
    def __str__(self):
        return f"Numero de cuenta: {self.__nCuenta}, Tipo de pago: {self.__tipo}, Importe: {self.__importe}"
    def __lt__(self,otro):
        return self.__nCuenta < otro.getNumCuenta()
