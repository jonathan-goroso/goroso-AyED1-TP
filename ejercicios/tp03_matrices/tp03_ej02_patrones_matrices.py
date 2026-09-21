def mostrar_matriz(matriz):

    for fila in matriz:
        for num in fila:
            print(f"{num:<3}",end=" ")
        print("")

def generar_matriz(num):

    matriz=[]
    for i in range(num):
        matriz.append([])
        for j in range(num):
            matriz[i].append(0)
    return matriz


def primera_matriz(num:int):
    matriz=generar_matriz(num)
    valor=1
    for i in range(num):
        matriz[i][i]=valor
        valor+=2
    print("primera matriz:")
    mostrar_matriz(matriz)

def segunda_matriz(num:int):
    matriz=generar_matriz(num)

    for i in range(num):
        matriz[i][num-1-i]= 3**(num-1-i)


    print("segunda matriz:")
    mostrar_matriz(matriz)

def tercera_matriz(num:int):
    matriz=generar_matriz(num)

    for i,fila in enumerate(matriz):
        fila[:i+1] = [num-i]*(i+1)

    print("tercera matriz:")
    mostrar_matriz(matriz)

def cuarta_matriz(num:int):
    matriz=generar_matriz(num)

    for i,fila in enumerate(matriz):
        for j in range(num):
            fila[j]= 2**(num-i-1)

    print("cuarta matriz:")
    mostrar_matriz(matriz)

def quinta_matriz(num:int):
    matriz=generar_matriz(num)

    agregar=1
    for i,fila in enumerate(matriz):
        if i%2:
            inicio=0
        else:
            inicio=1
        for j in range(inicio,num,2):
            fila[j]=agregar
            agregar+=1

    print("quinta matriz:")
    mostrar_matriz(matriz)

def sexta_matriz(num:int):
    matriz=generar_matriz(num)

    agregar=1
    for i,fila in enumerate(matriz):
        for j in range(num-1,num-2-i,-1):
            fila[j]=agregar
            agregar+=1


    print("sexta matriz:")
    mostrar_matriz(matriz)

def septima_matriz(num:int):
    matriz=generar_matriz(num)

    fila_inicio=0
    fila_final=num-1
    columna_inicio=0
    columna_final=num-1
    valor=1
    while fila_inicio<=fila_final and columna_inicio<=columna_final:

        for i in range(columna_inicio,columna_final+1):
            matriz[columna_inicio][i]=valor
            valor+=1
            print("derecha",valor)
        fila_inicio+=1
        
        for i in range(fila_inicio,fila_final+1):
            matriz[i][columna_final]=valor
            valor+=1
            print("abajo",valor)
        columna_final-=1

        for i in range(columna_final,columna_inicio-1,-1):
            matriz[fila_final][i]=valor
            valor+=1
            print("izquierda",valor)
        fila_final-=1
        
        for i in range(fila_final,fila_inicio-1,-1):
            matriz[i][columna_inicio]= valor
            valor+=1
            print("arriba",valor)
        columna_inicio+=1

    print("septima matriz:")
    mostrar_matriz(matriz)

def main():

    num = int(input("ingrese un numero: "))

    primera_matriz(num)
    segunda_matriz(num)
    tercera_matriz(num)
    cuarta_matriz(num)
    quinta_matriz(num)
    sexta_matriz(num)
    septima_matriz(num)

if __name__ == '__main__':

    main()