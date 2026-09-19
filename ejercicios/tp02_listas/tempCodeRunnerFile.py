def registrar_socios()->tuple[list[int],list[int]]:

    while True:
        lista_socios=[]
        cant_ingresos=[]
        socio = int(input("ingrese el numero de socio: "))

        if socio ==0:
            break
        elif 10000<socio<100000:
            if socio in lista_socios:
                cant_ingresos[lista_socios.index(socio)]+=1
            else:
                cant_ingresos.append(1)
                lista_socios.append(socio)
        else:
            print("numero de socio invalido")

    return lista_socios, cant_ingresos

def informar_ingresos(list_socios:list[int],cant_ingresos:list[int])->None:

    for i,socio in enumerate(list_socios):
        print(f"el socio {socio} ingreso {cant_ingresos[i]} veces")


def baja_socio(list_socios:list[int],cant_ingresos:list[int])->None:

    while True:
        baja = int(input("ingrese el numero de socio que se dio de baja: "))

        if baja in list_socios:
            break
        else:
            print("no existe ese numero de socio")

    for i,socio in enumerate(list_socios):
            print(f"el socio {socio} ingreso {cant_ingresos[i]} veces")

    cant_ingresos.remove(cant_ingresos[list_socios.index(baja)])
    list_socios.remove(baja)

    for i,socio in enumerate(list_socios):
        print(f"el socio {socio} ingreso {cant_ingresos[i]} veces")


def main():

    list_socios ,cant_ingresos = registrar_socios()

    informar_ingresos(list_socios, cant_ingresos)

    baja_socio(list_socios, cant_ingresos)

if __name__=='__main__':
    main()