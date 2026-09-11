
def diadelasemana(dia:int,mes:int,año:int)->int:
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

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

def crear_calendario(mes:int, año:int)->None:
    """
    crea un calendario en base al mes y año recibido
    pre:recibe dos enteros
    post:imprime por pantalla el resultado final
    """
    dias_meses={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dias_meses[2]= bisiesto(año)
    
    matriz_calendario=[["D","L","M","M","J","V","S"],[],[],[],[],[],]

    diasem = diadelasemana(1,mes,año)
    semana=1
    for dia in range(diasem):
        matriz_calendario[semana].append(" ")
    matriz_calendario[semana].append("1")
    for dia in range(2,dias_meses[mes]+1):

        diasem=diadelasemana(dia,mes,año)
        if diasem==6:
            matriz_calendario[semana].append(str(dia))
            semana+=1
        else:
            matriz_calendario[semana].append(str(dia))

    for fila in matriz_calendario:
        for elemento in fila:
            print(f"{elemento:<5}", end=" ")
        print()
    
def main():
    """
    funcion principal del programa
    """
    fecha = 12,9,2026    #aca podes elegir la fecha
    crear_calendario(fecha[1],fecha[2])


if __name__ == '__main__':

    main()