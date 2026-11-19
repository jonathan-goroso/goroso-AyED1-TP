def minimo_matriz(matriz: list[list[int]], fila: int = 0, columna: int = 0) -> int:

    if fila == len(matriz) - 1 and columna == len(matriz[fila]) - 1:
        return matriz[fila][columna]

    if columna == len(matriz[fila]) - 1:
        minimo = minimo_matriz(matriz, fila + 1, 0)
    else:
        minimo = minimo_matriz(matriz, fila, columna + 1)

    if matriz[fila][columna] < minimo:
        return matriz[fila][columna]

    return minimo


def main():
    matriz = [
        [8, 3, 6],
        [4, 1, 9],
        [7, 5, 2]
    ]

    print(minimo_matriz(matriz))

if __name__ == "__main__":
    main()