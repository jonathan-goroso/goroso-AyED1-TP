def calcular_producto(num1: int, num2: int) -> int:

    if num2 == 0:
        return 0

    return num1 + calcular_producto(num1, num2 - 1)


def main():

    num1 = 5
    num2 = 10
    print(calcular_producto(num1, num2))


if __name__ == "__main__":

    main()
