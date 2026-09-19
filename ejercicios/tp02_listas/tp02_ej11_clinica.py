
def mostrar_listado(turnos:list[int],urgencias:list[int])->None:
    """
    muestra a los pacientes atendidos de urgencia y los atendidos por turnos

    pre:
    post: imprime por pantalla la lista urgencias y turnos
    """

    if urgencias:
        print("los pacientes atendidos de urgencia fueron:")
        for n in urgencias:
            print(n,end=", ")
        print("")
    else:
        print("no hubo pacientes de urgencia")

    if turnos:
        print("los pacientes con turno fueron:")
        for n in turnos:

            print(n, end=", ")
        print("")
    else:
        print("nu hubo pacientes con turnos")

def buscar_afiliado(turnos:list[int], urgencias:list[int])->None:
    """
    cuenta cuantas urgencias y turnos tiene un afiliado

    pre:
    post: imprime por pantalla la cantidad de urgencias y turnos del afiliado
    """

    buscar = int(input("ingrese el numero de afiliado que quiere buscar: "))

    if buscar in turnos:
        print(f"el afiliado {buscar} tiene {turnos.count(buscar)} turnos")
    else:
        print(f"el afiliado {buscar} no tiene turnos")
    if buscar in urgencias:
        print(f"el afiliado {buscar} tubo {urgencias.count(buscar)} urgencias")
    else:
        print(f"el afiliado {buscar} no tubo urgencias")

def main():

    turnos = []
    urgencias = []
    while True:

        afiliado = int(input("ingrese su numero de afiliado: "))

        if afiliado == -1:
            break
        elif 999<afiliado<10000:
            prioridad = input("ingrese 0 si es una urgencia, 1 si es un turno: ")

            if prioridad == "0":
                urgencias.append(afiliado)
            elif prioridad == "1":
                turnos.append(afiliado)
            else:
                print("opcion invalida")
        else:
            print("numero de afiliado invalido")

    mostrar_listado(turnos,urgencias)

    buscar_afiliado(turnos,urgencias)

if __name__=='__main__':

    main()