from random import randint as rn
def generar_sala()->None:
    """
    genera el tamaño de la sala
    pre:
    post:devuelve una lista de listas de string
    """

    matriz=[]
    filas = int(input("ingrese cuantas filas tiene la sala: "))
    butacas = int(input("ingrese cuantas butacas tiene las filas: "))

    print("L: libre")
    print("R:Reservada")
    for i in range(filas):
        matriz.append([])
        for j in range(butacas):
            matriz[i].append("L")

    return matriz
def mostrar_butacas(sala:list[list[str]])->None:
    """
    muestra el estado de cada butaca de la sal
    pre:la matriz recibida deben ser listas con strings("L" o "R")
    post:imprime la matriz por pantalla
    """
    for fila in sala:
        print("")
        for butaca in fila:
            print(f"{butaca:<3}",end=" ")
    print("")

def reservar(sala:list[list[str]],reserva:tuple[int,int])->True|False:
    """
    reserva una butaca en caso de estar disponible
    pre:la matriz recibida deben ser listas con strings("L" o "R")
        la tupla debe tener enteros positivos
    post:devuelve un booleano
    """
    if 0<reserva[0]<=len(sala) and 0<reserva[1]<=len(sala[0]):

        if sala[reserva[0]-1][reserva[1]-1]=="L":
            sala[reserva[0]-1][reserva[1]-1]="R"
            return True
        else:
            print("la butaca ya esta ocupada asi que",end=" ")
            return False
    else:
        print("la butaca no existe asi que", end=" ")
        return False

def cargar_sala(sala:list[list[str]])->None:
    """
    carga la sala aleatoriamente
    pre:la matriz recibida deben ser listas con strings("L" o "R")
    post:la matriz queda cargada aleatoriamente
    """
    for i,fila in enumerate(sala):
        for j,butaca in enumerate(fila):
            if butaca !="R":
                num = rn(0,100)
                if num < 30:
                    sala[i][j]="R"
    print("sala reservada aleatoriamente:")

def butacas_libres(sala:list[list[str]])->int:
    """
    cuenta cuantas butacas libres hay en la sala
    pre:la matriz recibida deben ser listas con strings("L" o "R")
    post:devuelve un entero
    """
    libres = 0
    for fila in sala:
        libres+= fila.count("L")

    return libres

def butacas_contiguas(sala:list[list[str]])->tuple[int,int]:
    """
    busca la secuencia de butacas libres contiguas mas larga en una misma fila
    pre: la matriz recibida deben ser listas con strings "L" o "R"
    post:devuelve un tupla con las coordenas del comienzo de la secuencia mas larga
    """
    mayor=(0,0,0)
    for i,fila in enumerate(sala):
        contador = 0
        for j,butaca in enumerate(fila):
            if contador==0 and butaca=="L":
                contador+=1
                coordenadas = i,j
            elif butaca == "L":
                contador+=1
            else:
                if contador>mayor[0]:
                    mayor=(contador,) + coordenadas
                contador=0
        if contador>mayor[0]:
            mayor=(contador,) + coordenadas
            contador=0
    return mayor[1],mayor[2]



def main():

    sala=generar_sala()
    mostrar_butacas(sala)

    while True:
        print("ingrese -1 para dejar de reservar")
        fila = int(input("elija la fila en la que quiere estar: "))
        butaca = int(input("elija la butaca que quiera reservar: "))
        reserva = fila,butaca
        if fila!=-1 and butaca !=-1:
            if reservar(sala,reserva):
                print("butaca reservada")
                mostrar_butacas(sala)
            else:
                print("no se pudo reservar")
        else:
            print("")
            break

    cargar_sala(sala)
    mostrar_butacas(sala)
    print(f"La cantidad de butacas libres en la sala son {butacas_libres(sala)}")
    coordenadas = butacas_contiguas(sala)
    print(f"la secuencia de butacas libres mas largas empieza en la fila {coordenadas[0]+1} en la butaca {coordenadas[1]+1}")

if __name__== '__main__':

    main()