
def calcular_vuelto(vuelto:int)->None:
    """
    calcula cuantos billetes de cada denominacion tiene que devolver para el vuelto

    pre:

    post:inprime por pantalla el numero exacto de billetes de cada denominacio que se tiene que entregar
    """
    billetes=(5000,1000,500,200,100,50,10)
    contador_billetes =[0,0,0,0,0,0,0]

    for i , billete in enumerate(billetes):
        while True:
            if vuelto-billete >=0:
                vuelto -= billete
                contador_billetes[i]+=1
            else:
                break
    print("el vuelto debe contener")
    for cantidad, billete in zip(contador_billetes,billetes):
        print(f"{cantidad} billete de {billete}, ")
            
def main()->None:
    """
    funcion principal del programa
    """
    precio_total= int (input("ingrese el precio total: "))
    dinero_recibido= int(input("ingrese el dinero recibido "))

    assert dinero_recibido >= precio_total, "el dinero recibido no es suficiente"
    assert dinero_recibido %10 ==0,"el cambio no puede entregarse por falta de billetes con demnominaciones adecuadas"
    vuelto = dinero_recibido - precio_total

    calcular_vuelto(vuelto)

if __name__=='__main__':
    main()