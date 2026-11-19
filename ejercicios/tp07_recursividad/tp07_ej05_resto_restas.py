def calcular_resto(dividendo: int, divisor: int):


    if dividendo < divisor:
        return dividendo

    return calcular_resto(dividendo - divisor, divisor)

def main():

    num1=11
    num2=3

    if  num2 == 0:
        print("no se puede dividir por cero")
    else:
        print(f"resto {calcular_resto(num1,num2)}")


if __name__ == '__main__':

    main()