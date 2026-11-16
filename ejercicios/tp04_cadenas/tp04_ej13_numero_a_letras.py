def escribir(num: int, escrito: str):
    lista_num = [int(x) for x in str(num)[::-1]]
    unidades = {
        0: "",
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis",
        7: "siete",
        8: "ocho",
        9: "nueve",
    }
    decenas = {
        0: "",
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        2: "veinti",
        3: "treinta",
        4: "cuarenta",
        5: "cincuenta",
        6: "sesenta",
        7: "setenta",
        8: "ochenta",
        9: "noventa",
    }
    centenas = {0: "", 1: "ciento", 5: "quinientos", 7: "setecientos", 9: "novecientos"}

    if len(lista_num) > 1 and lista_num[1] != 0:
        if lista_num[1] == 1 and lista_num[0] < 6:
            escrito = decenas[int(str(lista_num[1]) + str(lista_num[0]))] + escrito
        elif lista_num[1] == 1:
            escrito = "dieci" + unidades[lista_num[0]] + escrito
        elif lista_num[1] == 2 and lista_num[0] == 0:
            escrito = "veinte" + escrito
        elif lista_num[1] == 2:
            escrito = decenas[lista_num[1]] + unidades[lista_num[0]] + " " + escrito
        else:
            escrito = (
                decenas[lista_num[1]] + " y " + unidades[lista_num[0]] + " " + escrito
            )

    if len(lista_num) == 1 or len(lista_num) > 1 and lista_num[1] == 0:
        escrito = unidades[lista_num[0]] + " " + escrito

    if len(lista_num) == 3:
        if lista_num[2] == 1 and lista_num[1] == 0 and lista_num[0] == 0:
            escrito = "cien" + " " + escrito
        elif lista_num[2] in centenas:
            escrito = centenas[lista_num[2]] + " " + escrito
        else:
            escrito = unidades[lista_num[2]] + "cientos" + " " + escrito

    return escrito


def main():
    niveles = ["mil", "millones", "mil millones"]
    num = int(input("ingrese un numero: "))
    escrito = ""
    i = 0

    while True:

        if len(str(num)) == 13:
            escrito = "un billon"
            break
        elif len(str(num)) > 13:
            escrito = "numero demasiado alto"
            break
        resto = num % 1000
        escrito = escribir(resto, escrito)
        num = num // 1000
        if num == 0:
            break
        else:
            escrito = niveles[i] + " " + escrito
            i += 1
    print(escrito)


if __name__ == "__main__":

    main()
