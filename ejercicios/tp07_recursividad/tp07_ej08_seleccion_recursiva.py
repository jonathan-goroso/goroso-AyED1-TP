def ordenar_lista(lista: list[int], inicio: int = 0) -> None:
    if inicio == len(lista):
        return

    posicion_menor = inicio

    for i in range(inicio + 1, len(lista)):
        if lista[i] < lista[posicion_menor]:
            posicion_menor = i

    lista[inicio], lista[posicion_menor] = lista[posicion_menor], lista[inicio]

    ordenar_lista(lista, inicio + 1)


def main():
    numeros = [8, 3, 6, 1, 9, 2]

    ordenar_lista(numeros)

    print(numeros)


if __name__ == "__main__":
    main()
