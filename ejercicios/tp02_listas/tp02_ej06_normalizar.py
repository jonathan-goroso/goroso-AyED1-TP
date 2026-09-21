from random import randint as rn
from functools import reduce

def generar_lista()->list[int]:

    lista=[]
    for i in range(5):
        lista.append(rn(1,10))
    return lista

def normalizar(lista:list[int])->list[float]:
    """
    normaliza la lista recibida respetando las proporciones relativas que cada elemento tiene en la lista original
    pre:recibeuna lista de enteros
    post:devuelve una lista de flotantes
    """

    #suma todos los elementos de la lista
    suma = reduce((lambda acumulador, elemento: acumulador + elemento), lista)

    #normaliza cada elemento de la lista
    normalizado = list(map(lambda elemento:elemento / suma ,lista))

    return normalizado

def main():

    lista=generar_lista()

    print(f"lista normal: {lista}")
    print(f"la lista normalizada es: {list(normalizar(lista))}")

if __name__=='__main__':

    assert normalizar([1,1,2])== [0.25,0.25,0.50]

    main()