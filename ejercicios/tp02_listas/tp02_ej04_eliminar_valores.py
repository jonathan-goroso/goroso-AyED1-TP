from random import randint as rn

def generar_listas()->tuple[list[int],list[int]]:
    """
    genera dos listas
    post: devulve una tupla de lista de enteros
    """
    lista1= []
    lista2 = []
    for i in range(11):
        lista1.append(rn(1,20))

    for i in range(5):
        lista2.append(rn(1,20))

    return lista1, lista2

def elminiar_elementos(original:list[int],eliminar:list[int])->None:
    """
    Elimina de una lista de números aquellos valores que se encuentren en una segunda lista
    pre:recibe 2 listas de enteros
    post:modifica la lista original
    """
    for n in eliminar:
            if n in original:
                for i in range(original.count(n)):
                    original.remove(n)

def main():

    lista_original,valores_eliminar=generar_listas()

    print(f"lista completa: {lista_original}")
    print(f"numeros a eliminar: {valores_eliminar}")

    elminiar_elementos(lista_original,valores_eliminar)

    print(f"lista filtrada: {lista_original}")

if __name__ == '__main__':
    main()