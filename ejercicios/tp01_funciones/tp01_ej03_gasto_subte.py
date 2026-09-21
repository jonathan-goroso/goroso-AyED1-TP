def calcular_gastos(viajes: int)->bool:
    """
    calcula el total gastado en viajes

    """

    tarifa = 2000
    total = 0
    if viajes <=20:
        total = viajes * tarifa
    elif viajes >20 and viajes <31:
        total = (viajes * tarifa) * 0.80
    elif viajes >30 and viajes <41:
        total = (viajes * tarifa) * 0.70
    else:
        total = (viajes * tarifa) * 0.60
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

    assert calcular_gastos(1)==2_000
    assert calcular_gastos(20)==40_000
    assert calcular_gastos(21)==33_600
    assert calcular_gastos(30)==48_000
    assert calcular_gastos(31)==43_400
    assert calcular_gastos(40)==56_000
    assert calcular_gastos(100)==120_000
    main()