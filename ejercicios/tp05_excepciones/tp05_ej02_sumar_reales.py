
def sumar_reales(num1,num2):

    try:

        num1=float(num1)
        num2=float(num2)

        return num1+num2

    except ValueError:
        return -1.0


def main():

    num1="12"
    num2="1.2"
    print(sumar_reales(num1,num2))



if __name__=='__main__':

    main()