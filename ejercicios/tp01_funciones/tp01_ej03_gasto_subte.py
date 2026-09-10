def calcular_gastos(viajes: int)->bool:
    """
    calcula el total gastado en viajes

    """

    tarifa = 2000
    total = 0
    if viajes <=20:
        total = viajes * tarifa
    elif viajes >20 and viajes <31:
        total = (viajes * tarifa) * 0.20
    elif viajes >30 and viajes <41:
        total = (viajes * tarifa) * 0.30
    else:
        total = (viajes * tarifa) * 0.30
    return total

def main():
    """
    funcion principal del programa
    """
    while True:
        viajes=int(input("ingrese la cantidad de viajes que hizo este mes: "))
        if viajes > 0:
            break
    print(f"el total gastado en viajes es: {calcular_gastos(viajes)}")


if __name__ == '__main__':
    main()