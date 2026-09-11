meses_con_31 = (1,3,5,7,8,10,12)
meses_con_30 = (4,6,9,11)

def pedir_fecha():
    """
    pide la fecha por teclado
    pre:
    post:devuelve 3 enteros
    """
    num1=int(input("ingrese un año: "))
    num2=int(input("ingrese un mes: "))
    num3=int(input("ingrese un dia: "))

    return num1,num2,num3
def concatenar_numeros(num1:int,num2:int,num3:int)-> int:
    """
    recibe 3 numeros y los concatena
    pre: los numeros tienen que se mayores a -1
    post: devuelve un numero como entero
    """
    lista_num1 = list(str(num1))
    lista_num2 = list(str(num2))
    lista_num3 = list(str(num3))

    lista_num1.extend(lista_num2)
    lista_num1.extend(lista_num3)

    numero_concatenado="".join(lista_num1)
    return int(numero_concatenado)

def bisiesto(año:int)->int:
    """
    recibe un año y verifica si es bisiesto o no
    pre:recibe un entero
    post:devuelve un entero
    """
    dias_febrero=28
    if año % 4 ==0 and año % 100 !=0 or año % 400 == 0 :
        dias_febrero=29
    return dias_febrero

def validar_fecha(dia: int,mes:int,año:int )-> True | False:
    """
    verifica si la fecha ingresada es valida
    pre: los elementos tienen que ser enteros mayores que 0
    post: devuelve True o False
    """   
    dias_febrero=bisiesto(año)

    if dia <= 31 and mes in meses_con_31:
        return True
    elif dia <= 30 and mes in meses_con_30:
        return True
    elif dia <= dias_febrero and mes == 2:
        return True
    else:
        return False

def fecha_siguiente(dia:int, mes:int,año:int)->tuple[int]:
    """
    devuelve la fecha del dia siguiente del la fecha recibida
    pre: recibe 3 enteros
    post: devuelve una tupla de enteros
    """

    if validar_fecha(dia+1,mes,año):
        dia+=1
    elif validar_fecha(1,mes+1,año):
        dia=1
        mes+=1
    else:
        dia=1
        mes=1
        año+=1
    return dia,mes,año

def diferencia_dias(dia:int,mes:int,año:int)->int:
    """
    en base a dos fechas calcula los dias de diferencia que tienen
    pre:recibe 3 enteros
    post:imprime por pantalla la diferencia de dias
    """
    print("ingrese la segunda fecha")
    año2,mes2,dia2=pedir_fecha()
    contador=0

    if concatenar_numeros(año,mes,dia) == concatenar_numeros(año2,mes2,dia2):
        print("es el mismo dia")
    elif concatenar_numeros(año,mes,dia) < concatenar_numeros(año2,mes2,dia2):
        while True:
            dia,mes,año=fecha_siguiente(dia,mes,año)
            contador+=1
            if concatenar_numeros(año,mes,dia)==concatenar_numeros(año2,mes2,dia2):
                print(F"la diferencia es de {contador} dias")
                break
    else:
        while True:
            dia2,mes2,año2=fecha_siguiente(dia2,mes2,año2)
            contador+=1
            if concatenar_numeros(año,mes,dia)==concatenar_numeros(año2,mes2,dia2):
                print(F"la diferencia es de {contador} dias")
                break
def main ()-> None:
    """
    funcion principal del programa
    """
    while True:
        año,mes,dia=pedir_fecha()

        if validar_fecha(dia,mes,año):
            dia_sig,mes_sig,año_sig=fecha_siguiente(dia,mes,año)
            print(f"el dia siguiente es {dia_sig}/{mes_sig}/{año_sig}")
            break
        else:
            print("fecha invalida, ingrese otra fecha")
    sumar_dias=int(input("ingrese la cantidad de dias que quiere sumarle: "))
    for i in range(sumar_dias-1):
        dia_sig,mes_sig,año_sig=fecha_siguiente(dia_sig,mes_sig,año_sig)
    print(f"despues de {sumar_dias} dias desde {dia}/{mes}/{año} la fecha es {dia_sig}/{mes_sig}/{año_sig}")

    diferencia_dias(dia,mes,año)
if __name__ == '__main__':
    main()