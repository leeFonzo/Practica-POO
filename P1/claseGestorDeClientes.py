import csv
from claseCliente import Cliente

class gestorClientes:
    __listaClientes: list
    def __init__(self):
        self.__listaClientes=[]

    def agregarCliente(self,uncliente):
        self.__listaClientes.append(uncliente)
    
    def test(self):
        titulo:bool=False
        try:
            archivo=open("ClientesFarmaCiudad.csv")
            reader=csv.reader(archivo, delimiter=";")
            for fila in reader:
                if titulo is False:
                    titulo=True
                else:
                    self.agregarCliente(Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4])))
                    print(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4]))
            archivo.close()
        except FileNotFoundError:
            print("no esta el archivo")
        except:
            print("ni idea mi loco pero todo salio mal")

    def getPosDNI(self, xdni):
        i:int=0
        band:bool=False
        pos:int=-1
        while i<len(self.__listaClientes) and band is False:
            if self.__listaClientes[i].getDNI()==xdni:
                pos=i
                band=True
            else:
                i+=1       
        return pos
    
    def actualizarSaldo(self, GM):
        xdni:int
        xnumC:int
        ayn:str
        saldo:float
        fecha:str
        desc:str
        tipo:str
        imp:float
        pos:int
        xdni=int(input("Ingrese DNI:"))
        pos=self.getPosDNI(xdni)
        if pos!=-1:
            xnumC=self.__listaClientes[pos].getNumCuenta()
            ayn=self.__listaClientes[pos].getApellido()+" "+self.__listaClientes[pos].getNombre()
            saldo=self.__listaClientes[pos].getSaldo()
            print(f"""
                    Cliente: {ayn}      Numero de cuenta: {xnumC}
                    Saldo Anterior: {saldo}

                                    Movimientos
                    Fecha       Descripcion     Importe     Tipo de Movimiento""")
            for i in range(GM._gestorMovimientos__cantidad):
                if GM._gestorMovimientos__listaMovimientos[i].getNumCuenta()==xnumC:
                    fecha=GM._gestorMovimientos__listaMovimientos[i].getFecha()
                    desc=GM._gestorMovimientos__listaMovimientos[i].getDescripcion()
                    tipo=GM._gestorMovimientos__listaMovimientos[i].getTipo()
                    imp=GM._gestorMovimientos__listaMovimientos[i].getImporte()
                    if tipo=="C":
                        saldo+=imp
                    elif tipo=="P":
                        saldo-=imp
                    print(f"""
                    {fecha}        {desc}         {imp}          {tipo}""")
                    print(f"""
                    Saldo Actualizado: {saldo}""")
        else:
            print("Error")

    def mostrarSinMovimientos(self, GM):
        xdni:int
        xnumC:int
        existe:bool
        xdni=int(input("Ingrese DNI: "))
        pos=self.getPosDNI(xdni)
        if pos!=-1:
            xnumC=self.__listaClientes[pos].getNumCuenta()
            existe=GM.existenMovimientos(xnumC)
            if existe is False:
                print("Este individuo roba quesos cremosos, su nombre y apellido es: ",self.__listaClientes[pos].getNombre()+" ",self.__listaClientes[pos].getApellido())
            else:
                print("No roba quesos cremosos")
        else:
            print("No se encontro usuario con ese DNI")
                  
