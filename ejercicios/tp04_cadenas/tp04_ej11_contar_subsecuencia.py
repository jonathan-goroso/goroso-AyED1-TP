def encontrar_subcadena(cadena: str, subcadena: str) -> int:
    """
    la funcion cuenta cuántas veces se encuentra una subcadena dentro de otra cadena,
    sin diferenciar mayúsculas y minúsculas

    pre:los parametro recibidos deben ser str
    post: retorna un entero
    """

    cadena = list(cadena.lower().strip())
    subcadena = list(subcadena.lower().strip())
    indice = 0
    contador = 0
    for letra in cadena:
        if subcadena[indice] == letra:
            indice += 1
        if indice > len(subcadena) - 1:
            indice = 0
            contador += 1

    return contador


def main():

    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro"
    subcadena = "uade"
    print(
        f"la cantidad de veces que aparece la subcadena es de {encontrar_subcadena(cadena,subcadena)} veces"
    )


if __name__ == "__main__":

    main()
