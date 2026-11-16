
def determinar_capicua(cadena:str)->bool:
    """
    la funcion determina si una cadena de caracteres es capicua o no
    pre:la funcion debe recibir un string
    post:devueve un booleano
    """

    for i,n in enumerate(cadena):
        if n != cadena[-(i+1)]:
            return False
    return True

def main():

    cadena="jonathan" 
    if determinar_capicua(cadena):
        print("es capicua")
    else:
        print("no es capicua")

if __name__=='__main__':

    assert determinar_capicua("hola")==False
    assert determinar_capicua("neuquen")==True
    main()
