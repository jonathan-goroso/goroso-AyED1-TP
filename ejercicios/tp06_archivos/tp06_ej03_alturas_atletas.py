class alturaError:
    pass


def GrabarRangoAlturas():

    disciplinas = []
    while True:
        atleta = 1

        disciplina = input("ingrese una disciplina (0 para salir): ")

        if disciplina == "0":
            break
        elif disciplina in disciplinas:
            print("ya ingreso esta disciplina")
            continue
        else:
            disciplinas.append(disciplina)

            try:
                with open("disciplinas.txt", "at", encoding="utf-8") as archivo:
                    archivo.write(disciplina + "\n")
            except OSError as error:
                print(f"ocurrio un error {error}")

        while True:

            try:
                altura = int(
                    input("ingrese la altura del atleta {atleta} (-1 para salir): ")
                )
                if altura < 100:
                    raise alturaError()
            except ValueError:
                print("la latura se tiene que representar solo con numeros")
            except alturaError:
                print("la altura minima es de 100 cm")
            else:

                if altura == "-1":
                    break

                try:
                    with open("disciplinas.txt", "at", encoding="utf-8") as archivo:
                        archivo.write(
                            "altura atleta " + str(atleta) + ":" + str(altura) + "\n"
                        )
                        atleta += 1
                except OSError as error:
                    print(f"ocurrio un error {error}")


def GrabarPromedio():
    alturas = []
    try:
        with open("disciplinas.txt", "rt", encoding="utf-8") as archivo:
            linea = archivo.readline()
            if ":" in linea:
                alturas.append(linea.strip().split(":").int(linea[1]))
            else:
                print(alturas)
                alturas = []
    except FileNotFoundError:
        print("archivo no encontrado")


def main():

    GrabarRangoAlturas()
    GrabarPromedio()


if __name__ == "__main__":

    main()
