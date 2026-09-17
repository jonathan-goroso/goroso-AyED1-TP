def main():
    num = int(input("ingrese un numero: "))

    lista= []
    for i in range(1,num+1):
        lista.append(i)

    #eleva al cuadrado a todos los elementos de la lista
    lista_cuadrados= list(map(lambda elemento: elemento**2, lista))

    if len(lista_cuadrados)<=10:
        print(lista_cuadrados)
    else:
        print(lista_cuadrados[-10:])


if __name__ == '__main__':
    main()