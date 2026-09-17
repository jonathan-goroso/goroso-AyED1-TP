
def verificar_orden(lista:list)->True | False:
    """
    verifica si la lista esta ordenada de forma ascendente
    pre: recibe una lista homogenea
    post:devuelve un booleano
    """
    if len(lista)>1:
        for i in range(1,len(lista)):
            if lista[i]<= lista[i-1]:
                return False
    return True

def main():

    lista = ["a","b","c"]
    if verificar_orden(lista):
        print("la lista esta ordenada de forma ascendente")
    else:
        print("no esta ordenada de forma ascendente")

if __name__ == '__main__':

    assert verificar_orden([1,2,3])==True
    assert verificar_orden([1,3,2])==False
    assert verificar_orden([1])==True
    assert verificar_orden(["a","b","c"])==True
    assert verificar_orden(["a","f","c"])==False

    main()