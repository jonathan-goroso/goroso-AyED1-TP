from random import randint as rn

def buscar_num(num:int,matriz:list[list[int]])->True|False:
    """
    busca si un numero se encuentra en la matriz
    pre:num es un entero positivo
        la matriz debe contener enteros 
    post:devuelve un booleano
    """
    valor = True
    for i in range(len(matriz)):
        if num in matriz[i]:
            valor = False
            break
    return valor

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

def generar_matriz()->list[list[int]]:
    """
    genera una matriz de N x N con números enteros al azar comprendidos
    en el intervalo [0,N**2), de tal forma que ningún número se repita
    pre:
    post:devuelve una matriz de enteros
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
            while True:
                num = rn(0,(tamaño**2)-1)
                if buscar_num(num,matriz):
                    break
            matriz[i].append(num)
    return matriz

def main():

    matriz = generar_matriz()
    mostrar_matriz(matriz)

if __name__ =='__main__':
    main() 