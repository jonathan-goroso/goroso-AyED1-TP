def imprimir_matriz(matriz: list[list[int]], fila: int = 0, columna: int = 0) -> None:

    if fila == len(matriz):
        return

    if columna == len(matriz[fila]):
        print()
        imprimir_matriz(matriz, fila + 1, 0)
        return

    print(f"{matriz[fila][columna]:5}", end="")

    imprimir_matriz(matriz, fila, columna + 1)


def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()