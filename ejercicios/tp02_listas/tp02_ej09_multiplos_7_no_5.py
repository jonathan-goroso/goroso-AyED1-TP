def main():

    a=int(input("ingrese un numero: "))
    b=int(input("ingrese un numero: "))

    if a > b:
        a,b = b, a

    #Genera una lista con numero entre A y B que sean múltiplos de 7 y que no sean múltiplos de 5
    lista = [n for n in range(a,b+1) if n %7==0 and n %5]

    print(lista)

if __name__=='__main__':
    main()