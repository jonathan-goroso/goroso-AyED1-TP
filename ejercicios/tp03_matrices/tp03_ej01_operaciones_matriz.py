def crear_matriz() -> list[list[int]]:
    """
    genera una matriz y el tamaño depende de lo que se ingrese por teclado
    pre:
    post:devuelve una lista de listas de enteros (una matriz de enteros)
    """
    matriz = []
    while True:
        tamaño = int(input("ingrese el tamaño de la matriz: "))
        if tamaño >= 2:
            break
        else:
            print("el tamaño de la matriz debe ser de minimo 2")
    for i in range(tamaño):
        matriz.append([])
        for j in range(tamaño):
            num = int(
                input("ingrese un numero para agregar hasta completar la matriz: ")
            )
            matriz[i].append(num)

    return matriz


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """
    muestra la matriz
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: imprime la matriz por pantalla
    """
    for i in range(len(matriz)):
        print("")
        for num in matriz[i]:
            print(f"{num:>3}", end=" ")
    print("")


def ordenar_matriz(matriz: list[list[int]]) -> None:
    """
    ordena cada fila de la matriz de forma ascendente
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: los elementos de las dos filas quedan ordenasdas ascendentemente
    """
    print("lista ordenada de forma ascendente en cada fila")
    for indice in range(len(matriz)):
        matriz[indice].sort()

    mostrar_matriz(matriz)


def intercambiar_filas(matriz: list[list[int]]) -> None:
    """
    intercambia los elementos entre dos filas de la matriz
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: los elementos de la dos filas seleccionadas son intercambiadas
    """
    fila1 = int(input("elija un fila: "))
    fila2 = int(input("elija con cual fila intercambiar: "))

    for i in range(len(matriz)):
        matriz[fila1 - 1], matriz[fila2 - 1] = matriz[fila2 - 1], matriz[fila1 - 1]

    mostrar_matriz(matriz)


def intercambiar_columnas(matriz: list[list[int]]) -> None:
    """
    intercambia los elementos entre dos columnas de la matriz
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: los elementos de la dos columnas seleccionadas son intercambiadas
    """
    columna1 = int(input("elija un columna: "))
    columna2 = int(input("elija con cual culumna intercambiar: "))

    for i in range(len(matriz)):
        matriz[i][columna1 - 1], matriz[i][columna2 - 1] = (
            matriz[i][columna2 - 1],
            matriz[i][columna1 - 1],
        )

    mostrar_matriz(matriz)


def trasponer_matriz(matriz: list[list[int]]) -> None:
    """
    intercambia la filas por la columanas y la columnas por las filas
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: las filas y las columnas quedan intercambiadas
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

    print("matriz transpuesta")
    mostrar_matriz(matriz)


def calcular_promedio(matriz: list[list[int]]) -> float:
    """
    calcula el promedio de una fila
    pre:los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: devuelve un float
    """

    fila = int(input("elija a cual fila calcular el promedio: "))

    suma = 0
    for n in matriz[fila - 1]:
        suma += n

    return suma / len(matriz)


def calcular_porcentaje(matriz: list[list[int]],columna:int)->float:
    """
    calcula el procentaje de elementos impares en una columna
    pre:los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
        columna debe ser un entero positivo
    post:devuelve un float
    """
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][columna - 1] % 2:
            contador += 1

    return (contador / len(matriz)) * 100


def simetria_diagonal_principal(matriz: list[list[int]])->True|False:
    """
    Determina si la matriz es simétrica con respecto a su diagonal principal
    pre:los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: devuelve un booleano
    """
    simetrico = False
    for i in range(len(matriz) - 1):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                simetrico = True
    return simetrico

def simetria_diagonal_secundaria(matriz: list[list[int]])->True|False:
    """
    Determina si la matriz es simétrica con respecto a su diagonal secundarua
    pre:los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: devuelve un booleano
    """

    simetrico = False
    for i in range(len(matriz) - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            if matriz[i][j] != matriz[j][i]:
                simetrico = True
    return simetrico

def determinar_capicuas(matriz: list[list[int]])->list[int]:
    """
    determina que columnas de la matriz son capicuas
    pre:los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: devuelve una lista de enteros
    """
    columnas_capicua = []

    for i in range(len(matriz)):
        capicua = True
        largo = len(matriz)
        for j in range(len(matriz)):
            if matriz[j][i] == matriz[largo - 1][i]:
                largo -= 1
            else:
                capicua = False
                break
        if capicua:
            columnas_capicua.append(i)
    return columnas_capicua

def main():

    matriz = crear_matriz()
    mostrar_matriz(matriz)
    ordenar_matriz(matriz)
    intercambiar_filas(matriz)
    intercambiar_columnas(matriz)
    trasponer_matriz(matriz)

    print(f"el promedio de la fila es {calcular_promedio(matriz)}")

    columna = int(input("elija una columna para calcular el porcentaje de impares: "))
    print(f"el porcentaje es de un {calcular_porcentaje(matriz,columna)} %")

    if simetria_diagonal_principal(matriz):
        print("la matriz no es simetrica con respecto a su diagonal principal")
    else:
        print("la matriz es simetrica con respecto a su diagonal principal")

    if simetria_diagonal_secundaria(matriz):
        print("la matriz no es simetrica con respecto a su diagonal secundaria")
    else:
        print("la matriz es simetrica con respecto a su diagonal secundaria")

    capicuas = determinar_capicuas(matriz)
    if capicuas:
        print(f"la columnas capicuas son {capicuas}")
    else:
        print("no hay columnas capicuas")

if __name__ == "__main__":
    main()
