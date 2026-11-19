class menorUnoError(Exception):

    pass


def sumar_naturales(num: int) -> int:

    if num == 1:
        return 1

    return num + sumar_naturales(num - 1)


def main():
    try:
        num = int(input("ingrese un numero natural: "))
        if num < 1:
            raise menorUnoError()
    except ValueError:
        print("solo se permiten numeros naturales")
    except menorUnoError:
        print("el numero debe ser mayor a cero")
    else:
        print(sumar_naturales(num))


if __name__ == "__main__":

    main()
