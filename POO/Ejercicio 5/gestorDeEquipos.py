from Equipo import Equipo
import csv

class gestorEquipos:
    __equipos:list
    def __init__(self):
        self.__equipos=[]
    def agregarEquipo(self, nuevoEquipo):
        self.__equipos.append(nuevoEquipo)
    def test(self):
        archivo=open("equipos2024.csv")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            self.agregarEquipo(Equipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4])))
        archivo.close()