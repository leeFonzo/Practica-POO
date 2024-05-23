#De cada Equipo se registran: identificador del equipo, nombre del equipo, goles a favor, goles en
#contra, diferencia de goles, y puntos

class Equipo:
    __id:int
    __name:str
    __gf:int
    __gc:int
    __dg:int
    __pts:int
    def __init__(self, id, name, gf, gc, dg, pts):
        self.__id=id
        self.__name=name
        self.__gf=gf
        self.__gc=gc
        self.__dg=dg
        self.__pts=pts
    def getId(self):
        return self.__id
    def getname(self):
        return self.__name
    def getgf(self):
        return self.__gf
    def getgc(self):
        return self.__gc
    def getdg(self):
        return self.__dg
    def getpj(self):
        return self.__pts
    
        