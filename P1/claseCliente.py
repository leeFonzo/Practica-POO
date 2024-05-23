class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __nCuenta: int
    __saldoAnterior: float
    
    def __init__(self, nombre, apellido, dni, nCuenta, saldoAnterior):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__nCuenta=nCuenta
        self.__saldoAnterior=saldoAnterior

    def getDNI(self):
        return self.__dni

    def getNumCuenta(self):
        return self.__nCuenta

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSaldo(self):
        return self.__saldoAnterior

    def __lt__(self,otro):
        return self.__nCuenta < otro.getNumCuenta()

    def __str__(self):
        return f"Nombre:{self.__nombre} {self.__apellido}, DNI:{self.__dni}"
