def sumar_matriz(matriz: list[list[int]], fila: int = 0, columna: int = 0) -> int:

    if fila == len(matriz):
        return 0

    if columna == len(matriz[fila]):
        return sumar_matriz(matriz, fila + 1, 0)

    return matriz[fila][columna] + sumar_matriz(matriz, fila, columna + 1)


def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(sumar_matriz(matriz))


if __name__ == "__main__":
    main()