from random import randint as rn
from functools import reduce

def generar_lista()->list[int]:
    """
    genera una lista al azar con numeros de 4 digitos. la cantidad de elementos tambien es un numero al azar de 2 digitos
    post:Devuelve una lista de enteros
    """
    cantidad= rn(10,99)
    lista=[]

    for i in range(cantidad):
        lista.append(rn(1000,9999))
    return lista

def verificar_capicua(lista:list[int])-> True | False:
    """
    revisa si la lista es capicua, True si es capicua o False si no
    pre:recibe una lista de enteros
    post: devuelve un booleano
    """
    for i in range(len(lista)):
        if i != -i:
            return False
    return True

def main():
    """
    funcion principal del programa
    """
    lista = generar_lista()
    print(f"la lista generada es: {lista}")

    # calcula y devuelve el producto de todos los elementos de la lista
    print(f"el producto de la lista es: {reduce((lambda acumulador,elemento: acumulador*elemento),lista)}")

    # elimina todas la apariciones de un numero, el numero a eliminar lo recibe por teclado
    num = int(input("ingrese que numero quiere eliminar: "))
    print(f"la lista nueva es {list(filter(lambda numero: numero != num, lista))}")

    valor=verificar_capicua(lista)

    if valor:
        print("es capicua")
    else:
        print("no es capicua")

if __name__=='__main__':
    main()