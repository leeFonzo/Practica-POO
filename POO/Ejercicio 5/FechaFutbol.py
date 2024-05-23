"""e cada Fecha de fútbol se registran: fecha del partido, identificador de equipo local, identificador
de equipo visitante, cantidad de goles que hizo el equipo local, cantidad de goles que hizo el equipo
visitante."""

class FechaDeFutbol:
    __fecha:str
    __idLocal:int
    __idVisitante:int
    __gfLocal:int
    __gfVisitante:int
    def __init__(self, fecha, idLocal, idVisitante, gfLocal, gfVisitante):
        self.__fecha=fecha
        self.__idLocal=idLocal
        self.__idVisitante=idVisitante
        self.__gfLocal=gfLocal
        self.__gfVisitante=gfVisitante
    def getFecha(self):
        return self.__fecha
    def getIdLocal(self):
        return self.__idLocal
    def getIdVisitante(self):
        return self.__idVisitante
    def getGfLocal(self):
        return self.__gfLocal
    def getGfVisitante(self):
        return self.__gfVisitante