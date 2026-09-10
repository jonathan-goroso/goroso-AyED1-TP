
def concatenar_numeros(num1: int,num2: int)-> str:
    """
    recibe dos nuemros y los concatena

    pre: los numeros tienen que se mayores a -1

    post: devuelve los numeros concatenados como string
    """
    lista_num1 = list(str(num1))
    lista_num2 = list(str(num2))

    lista_num1.extend(lista_num2)

    numero_concatenado="".join(lista_num1)

    return numero_concatenado

def main():

    while True:
        num1= int(input("ingrese el primer numero: "))
        num2= int(input("ingrese el segundo numero: "))

        if num1 >=0 and num2 >=0:
            break
        else:
            print("ingrese numeros poitivos")

    print(concatenar_numeros(num1, num2))

if __name__=='__main__':

    main()