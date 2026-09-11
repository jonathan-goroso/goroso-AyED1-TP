from random import randint as rn

def pesar_naranjas(cantnaranjas: int)->tuple[list[int],int]:
    """
    asigna aleatoriamente un peso a cada naranja y luego las clasifica como jugo si el peso se encuentra fuera del rango
    pre:recibe un entero
    post:devuelve una tupla con una lista de enteros y un entero
    """
    jugo=0
    naranjas=[]
    for naranja in range(cantnaranjas):
        peso = rn(150,350)

        if 199<peso<301:
            naranjas.append(peso)
        else:
            jugo+=1
    return naranjas,jugo

def contar_cajones(lista_pesos:list[int])->list[int]:
    """
    cuenta cuntos cajones se pueden llenar
    pre:recibe una lista de enteros
    post:devuelve una lista de enteros
    """
    pesototal=0
    limite=0
    peso_cajones=[]
    for peso in lista_pesos:
        pesototal+=peso
        limite+=1
        if limite==100:
            peso_cajones.append(pesototal)
            pesototal=0
            limite=0
    return peso_cajones

def contar_camiones(peso_cajones:list[int])->int:
    """
    cuenta cuantos camiones se necesitan para tranpostar la cosecha
    pre:se recibe una lista de enteros
    post: se retorna iun entero
    """
    camiones=0
    pesocamion=0
    for peso in (peso_cajones):
        pesocamion +=peso
        if pesocamion>500000:
            camiones+=1
            pesocamion=peso
    if pesocamion>=400000:
        camiones+=1
    return camiones

def main():
    """
    funcion principal del programa
    """
    cantnaranjas= int(input("ingrese la cantidad de naranjas cosechadas: "))

    peso_naranjas,cantjugo=pesar_naranjas(cantnaranjas)
    cantcajones=contar_cajones(peso_naranjas)
    cantcamiones=contar_camiones(cantcajones)
    print(f"{cantjugo} naranjas se clasifican para jugo")
    print(f"se pueden llenar {len(cantcajones)} cajones")
    if cantcamiones>0:
        print(f"para trasportar la cosecha se necesitan {cantcamiones} camiones")
    else:
        print("no se alcanza el peso minimo para 1 camion")
    print(f"hay un sabrante de {(cantnaranjas-cantjugo)%100} naranjas para el siguiente reparto")

if __name__ == '__main__':
    main()