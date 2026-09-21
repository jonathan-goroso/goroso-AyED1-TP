from random import randint as rn

def generar_matriz(fabricas:int)->list[list[int]]:

    matriz = []
    for i in range(fabricas):
        matriz.append([])
        for j in range(6):
            matriz[i].append(rn(0,150))
    return matriz

def mostrar_matriz(matriz: list[list[int]]) -> None:
    """
    muestra la matriz
    pre: los elementos de la lista recibida deben ser listas y esas lista deben tener enteros
    post: imprime la matriz por pantalla
    """

    for i in range(len(matriz)):
        print("")
        print(f"fabrica {i+1}:",end=" ")
    
        for num in matriz[i]:
            print(f"{num:>3}", end=" ")
    print("")

def total_por_fabrica(matriz:list[list[int]])->None:
    """
    cuenta el total fabricado por cada fabrica
    pre: la matriz tiene enteros entre 0 y 150
    post:imprime por pantalla el total de produccion de cada fabrica
    """

    print("el total producido por cada fabrica es:")
    for i in range(len(matriz)):
        
        print(f"fabrica {i+1}: {sum(matriz[i])} unidades")

def mayor_produccion(matriz:list[list[int]],dias:list[str])->None:
    """
    muestra cual fue la fabrica que mas produjo en un solo dia
    pre:la matriz tiene enteros entre 0 y 150
        la lista recibida debe contener string
    post:imprime por pantalla la fabrica y el dia
    """
    mayor = 0,0
    for i in range(len(matriz)):
        for j, num in enumerate(matriz[i]):
            if matriz[mayor[0]][mayor[1]]< num:
                mayor = i,j
    print(f"El que mas produjo fue la fabrica {mayor[0]+1} el {dias[mayor[1]]}")

def dia_mas_productivo(matriz:list[list[int]],dias:list[str])->None:
    """
    muestra cual fue el dia mas productivo
    pre:la matriz tiene enteros entre 0 y 150
        la lista recibida debe contener string
    post: imprime por pantalla el dia y la cantidad producida 
    """
    mayor=-1,0
    for i in range(len(matriz)):
        suma=0
        for j in range(len(matriz)):
            suma+=matriz[j][i]
        if suma > mayor[0]:
            mayor = suma , i

    print(f"El dia mas productivo fue {dias[mayor[1]]} con {mayor[0]} unidades")

def menor_catidad(matriz:list[list[int]])->None:
    """
    crea una lista que tiene la menor produccion de cada fabrica
    pre:la matriz tiene enteros entre 0 y 150
    post:crea la lista y la imprime por pantalla
    """
    menor_produccion = [min(fila) for fila in matriz]

    print(f"La menor produccion de cada fabrica es:")
    for i ,num in enumerate(menor_produccion):
        print(f"fabrica {i+1}: {num} unidades")

def main()->None:
    """
    funcion principal del programa
    """
    dias =["lunes","martes","miercoles","jueves","viernes","sabado"]
    fabricas = int(input("ingrese la cantidad de fabricas: "))

    matriz=generar_matriz(fabricas)
    mostrar_matriz(matriz)
    total_por_fabrica(matriz)
    mayor_produccion(matriz,dias)
    dia_mas_productivo(matriz,dias)

    lista = menor_catidad(matriz)
    

if __name__ == '__main__':

    main()