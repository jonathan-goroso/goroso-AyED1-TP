from math import sqrt


class negativoError(Exception):
    pass


def main():

    try:
        num = float(input("ingrese un numero: "))

        if num < 0:
            raise negativoError()

    except ValueError:
        print("solo se acepta numeros")
    except negativoError:
        print("no se pede sacar la raiz a un numero negativo")
    except Exception as e:
        print(f"hubo otro error {e}")
    else:
        print(f"la raiz de {num} es {sqrt(num)}")


if __name__ == "__main__":

    main()
