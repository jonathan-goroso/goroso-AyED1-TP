def main():

    palos = ["Oros", "Copas", "Espada", "Bastos"]

    baraja = [str(num) + " " + palo for palo in palos for num in range(1, 13)]

    print(baraja)


if __name__ == "__main__":

    main()
