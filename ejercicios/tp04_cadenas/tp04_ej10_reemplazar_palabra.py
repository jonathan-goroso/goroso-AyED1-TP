def reemplazar_palabras(cadena: str, palabra: str, reemplazo: str):
    contador = 0
    lista_frase = cadena.split(" ")
    for i in range(len(lista_frase)):
        if palabra == lista_frase[i]:
            lista_frase[i] = reemplazo
            contador += 1

    return " ".join(lista_frase), contador


def main():

    cadena = "El gato duerme en el sillón mientras el gato del vecino juega con una pelota y el gato chiquito corre por el patio"
    palabra = "gato"
    reemplazo = "perro"

    nueva_palabra, contador = reemplazar_palabras(cadena, palabra, reemplazo)

    print(f"palabra nueva:\n{nueva_palabra}\ncantidad de reemplazos {contador}")


if __name__ == "__main__":

    assert reemplazar_palabras("hace mucho calor", "calor", "frio") == (
        "hace mucho frio",
        1,
    )
    main()
