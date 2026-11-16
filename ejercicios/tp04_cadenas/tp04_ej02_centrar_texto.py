def main():

    cadena="hola"
    espacio = (80-len(cadena))//2

    cadena=(" "*espacio) + cadena +(" "*espacio)

    print(cadena)

if __name__=='__main__':

    main()