def contar_digitos(numero):

    numero = numero // 10

    if numero == 0:
        return 1

    return 1 + contar_digitos(numero)


def main():
    
    while True:
        try:
            num = int(input("ingrese un numero: "))
            break
        except ValueError:
            print("tiene que ser un numero entero")

    print(f" el {num} tiene {contar_digitos(abs(num))} digitos")
    


if __name__ == "__main__":

    main()
