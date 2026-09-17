from random import randint as rn

def generar_lista()->list[int]:
    """
    genera una lista con numeros aleatorios de 1 a 100
    post:retorna una lista de enteros
    """
    lista=[]
    for i in range(20):
        lista.append(rn(1,100))

    return lista

def main():

    lista=generar_lista()

    #genera una nueva lista solo con los numeros impares de la lista original
    num_impares = list(filter(lambda n: n%2, lista))

    print(f"lista original: {lista}")
    print(f"lista solo de impares: {num_impares}")

if __name__=='__main__':

    main()