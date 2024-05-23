from claseGestorDeClientes import gestorClientes
from claseGestorDeMovimientos import gestorMovimientos

def menu():
    op:int
    try:
        op=int(input("""
                                Menu
                1. Ingresar DNI par actualizar saldo
                2. Ingresar DNI para mostrar nya si no tiene movimientos
                3. Ordenar movimientos por N° de cuenta
                0. Pichula triste
                ..."""))
    except:
        print("La respuesta debe ser un entero")
        op=menu()
    return op

if __name__=='__main__':
    opcion:int
    GC=gestorClientes()
    GM=gestorMovimientos()
    GC.test()
    GM.test()
    opcion=menu()
    while opcion!=0:
        if opcion ==1:
            GC.actualizarSaldo(GM)
        elif opcion==2:
            GC.mostrarSinMovimientos(GM)       
        elif opcion==3:
            GM.ordenar()
            GM.listar()
        else:
            print("cualquiera")
        opcion=menu()
    print("gracias papu.¿")