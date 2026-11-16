from random import randint as rn


def main():

    adivinar = rn(1, 500)
    intentos = 0

    while True:
        try:
            num = int(input("ingrese un numero: "))

        except ValueError:
            print("solo se permiten numeros enteros")
            intentos += 1
        else:
            if num < adivinar:
                print("el numero que tiene que adivinar es mayor")
                intentos += 1
            elif num > adivinar:
                print("el numero que tiene que adivinar es menor")
                intentos += 1
            else:
                intentos += 1
                break

    print(f"¡ADIVINASTE! el numero era {adivinar}, te tomo {intentos} intentos")


if __name__ == "__main__":

    main()
