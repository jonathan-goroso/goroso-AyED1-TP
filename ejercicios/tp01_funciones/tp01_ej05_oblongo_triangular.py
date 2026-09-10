
def main()-> None:

    numero= int(input("ingrese un numero: "))

    oblongo = (lambda dato: int(dato**0.5)*(int(dato**0.5)+1)==dato)

    if oblongo(numero):
        print("es oblongo")
    else:
        print("no es oblongo")




if __name__ == '__main__':

    main()