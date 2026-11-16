def main():

    def validar_numero(texto: str) -> int | str:
        try:
            num = int(input(texto))
            return num
        except ValueError:
            print("Solo se permiten numeros enteros")
            return ""

    lista = []

    while True:

        num = validar_numero("ingrese un numero (-1 para finalizar): ")

        if num == "":
            continue
        elif num == -1:
            break
        lista.append(num)

    intentos = 3
    while intentos > 0:

        buscar = validar_numero(
            "ingrese un numero para ver su pocision (-1 para salir): "
        )
        if buscar == "":
            continue
        elif buscar == -1:
            break
        try:
            print(f"el {buscar} se encuentra en la pocision {lista.index(buscar)+1}")
        except ValueError:
            intentos -= 1
            print(f"no se encontro el numero ingresado, quedan {intentos} intentos")

    print("fin del programa")

if __name__ == "__main__":

    main()
