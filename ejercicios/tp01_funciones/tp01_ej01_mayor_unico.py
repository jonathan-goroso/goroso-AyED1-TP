#tp1 ej 1

def mayor_estricto(lista1: list[int]) -> int:
    """
    recibe una lista de enteros y busca el mayor. Si hay 2 numeros mayores iguales devuelve -1,
    sino devuelve el unico numero mayor

    """
    mayor = max(lista1)
    cantidad = lista1.count(mayor)
    if cantidad > 1:
        return -1
    else:
        return mayor

def main() -> None:
    """
    funcion principal del programa
    """
    lista = []
    while True:
        num = int (input("ingrese un numero: "))
        if num >0:
            lista.append(num)
            if len(lista)>2:
                break
    valor = mayor_estricto(lista)

    if valor >=-1:
        print(f"el mayor es {valor}")
    else:
        print("no hay un unico numero mayor")


if __name__ == '__main__':

    assert mayor_estricto([1, 2, 3]) == 3
    assert mayor_estricto([1, 3, 3]) == -1
    assert mayor_estricto([3, 2, 3]) == -1
    assert mayor_estricto([3, 2, 1]) == 3
    main()