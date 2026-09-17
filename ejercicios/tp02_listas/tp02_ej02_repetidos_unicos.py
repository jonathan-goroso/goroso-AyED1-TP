from random import randint as rn

def generar_lista(num:int)->list[int]:
    """
    genera una lista con numeros aleatorios del 1 al 100, la longitud de la lista depende del num recibido
    pre:recibe un entero
    post:retorna una lista de enteros
    """
    lista=[]
    for i in range(num):
        lista.append(rn(1,100))
    return lista

def buscar_repetido(lista:list[int])-> True | False:
    """
    revisa si hay elementos repetidos en la lista
    pre:recibe una ista de enteros
    post: retorna True o False
    """
    for n in lista:
        if lista.count(n)>1:
            return True
    return False

def eliminar_repetidos(lista:list[int])-> list[int]:
    """
    elimina los elementos repetidos de la lista
    pre:recibe una lista de enteros
    post:devuelve una lista de enteros
    """
    lista_nueva =[]

    for n in lista:
        if lista.count(n)==1:
            lista_nueva.append(n)
    return lista_nueva

def main()->None:
    """
    funcion principal del programa
    """
    num=int(input("ingrese un numero: "))
    lista=generar_lista(num)
    print(f"lista orginal: {lista}")

    if buscar_repetido(lista):
        print(f"lista sin elementos repetidos: {eliminar_repetidos(lista)}")
    else:
        print("no tiene elementos repetidos")

if __name__ == '__main__':
    main()