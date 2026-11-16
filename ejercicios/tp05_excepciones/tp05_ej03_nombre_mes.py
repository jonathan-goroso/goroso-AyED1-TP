class mesError(Exception):
    pass


def devolver_mes(num):

    meses = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ]

    try:

        num = int(num)
        if 0 < num < 13:
            return meses[num - 1]
        
        raise mesError()

    except ValueError:
        print("debe ingresar un numero entero")
    except mesError:
        print("solo se aceptan numeros del 1 al 12")

    return ""


def main():

    while True:
        num = input("ingrese un numero del mes: ")

        mes = devolver_mes(num)
        if mes != "":
            print(mes)
            break


if __name__ == "__main__":

    main()
