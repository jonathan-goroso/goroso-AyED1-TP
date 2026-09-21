
def validar_fecha(dia: int,mes: int, año: int )-> True | False:
    """
    verifica si la fecha ingresada es valida

    pre: dia, mes , año tienen que ser numeros enteros

    post: devuelve True si la fecha es valida y False si no lo es

    """   
    dias_febrero=28
    meses_con_31 = [1,3,5,7,8,10,12]
    meses_con_30 = [4,6,9,11]

    if año % 4 ==0 and año % 100 !=0 or año % 400 == 0 :
        dias_febrero=29
    if dia <= 31 and mes in meses_con_31:
        return True
    elif dia <= 30 and mes in meses_con_30:
        return True
    elif dia <= dias_febrero and mes == 2:
        return True
    else:
        return False
def main ()-> None:
    """
    funcion principal del programa
    """

    año = int(input("ingrese un año: "))
    mes = int(input("ingrese un mes: "))
    dia = int(input("ingrese un dia: "))

    valido=validar_fecha(dia,mes,año)

    if valido:
        print("fecha valida")
    else:
        print("fecha invalida")

if __name__ == '__main__':

    assert validar_fecha(29,2,2020)==True
    assert validar_fecha(29,2,2019)==False
    assert validar_fecha(31,3,2018)== True
    main()