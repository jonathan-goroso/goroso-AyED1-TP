class alturaError:
    pass


def GrabarRangoAlturas() -> None:

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
                if altura == -1:
                    break
                elif altura < 100:
                    raise alturaError()
            except ValueError:
                print("la altura se tiene que representar solo con numeros")
            except alturaError:
                print("la altura minima es de 100 cm")
            else:

                try:
                    with open("disciplinas.txt", "at", encoding="utf-8") as archivo:
                        archivo.write(
                            "altura atleta " + str(atleta) + ":" + str(altura) + "\n"
                        )
                        atleta += 1
                except OSError as error:
                    print(f"ocurrio un error {error}")


def GrabarPromedio() -> None:
    alturas = []
    try:
        with open("disciplinas.txt", "rt", encoding="utf-8") as archivo:
            linea = archivo.readline()
            with open("Promedios.txt", "at", encoding="utf-8") as arch:
                arch.write(linea)
                while True:
                    linea = archivo.readline()
                    if not linea:
                        break
                    elif ":" in linea:
                        dato = linea.strip().split(":")
                        alturas.append(int(dato[1]))
                    else:
                        arch.write(f"{sum(alturas)/len(alturas)}\n")
                        arch.write(linea)
                arch.write(f"{sum(alturas)/len(alturas)}\n")

    except FileNotFoundError:
        print("archivo no encontrado")
    except OSError as error:
        print(f"ocrrio un error {error}")


def PromedioGeneral():

    alturas = []
    deportes = []
    with open("promedios.txt", "rt", encoding="utf-8") as archivo:
        while True:

            linea = archivo.readline()
            linea=linea.strip()
            if not linea:
                break
            elif linea.isalpha():
                deportes.append(linea)
            else:
                alturas.append(float(linea))

    promedio = sum(alturas) / len(alturas)
    print("las diciplinas que superan el promedio son:")
    for i in range(len(alturas)):
        if alturas[i] > promedio:
            print(deportes[i])


def main():

    GrabarRangoAlturas()
    GrabarPromedio()
    PromedioGeneral()


if __name__ == "__main__":

    main()
