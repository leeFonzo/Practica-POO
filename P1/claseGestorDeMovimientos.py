import csv
import numpy as np
from claseMovimiento import Movimiento

class gestorMovimientos:
    __listaMovimientos:np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self):
        self.__cantidad=0
        self.__dimension=21
        self.__incremento=1
        self.__listaMovimientos=np.empty(self.__dimension, dtype=Movimiento)
        
    
    def agregarMovimiento(self, unMovimiento):
        if self.__cantidad==self.__dimension:
            self.__dimension +=self.__incremento
            self.__listaMovimientos.resize(self.__dimension)
        self.__listaMovimientos[self.__cantidad]=unMovimiento
        self.__cantidad+=1

    def test(self):
        try:
            archivo=open("MovimientosAbril2024.csv")
            reader=csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarMovimiento(Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
            archivo.close()
        except:
            print("Hubo un error en la carga")
    
    def existenMovimientos(self, xnumC):
        band:bool=False
        i:int=0
        while i<self.__cantidad and band is False:
            if self.__listaMovimientos[i].getNumCuenta()==xnumC:
                band=True
            else:
                i+=1
        return band
    
    def ordenar(self):
        self.__listaMovimientos=np.sort(self.__listaMovimientos)
        print("Los movimientos fueron ordenados por Numero de cuenta")

    def listar(self):
        for movimiento in self.__listaMovimientos:
            print(movimiento)