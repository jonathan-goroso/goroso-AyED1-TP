def eliminar_subcadena_sin_rebanadas(frase:str,comienzo:int,caracteres:int)->str:

    frase_filtrada=[frase[i] for i in range(len(frase)) if i<comienzo or i>comienzo+caracteres-1]
    return "".join(frase_filtrada)

def eliminar_subcadena_con_rebanadas(frase:str,comienzo:int,caracteres:int)->str:
    frase_filtrada=frase[:comienzo] + frase[comienzo + caracteres:]
    return frase_filtrada

def main():

    frase="El perro corre por el parque mientras los chicos juegan a la pelota y disfrutan del día"
    comienzo=38
    caracteres=30
    print(f"funcion sin rebanadas: \n{eliminar_subcadena_sin_rebanadas(frase,comienzo,caracteres)}")
    print(f"funcion con rebanas:\n{eliminar_subcadena_con_rebanadas(frase,comienzo,caracteres)}")

if __name__=='__main__':

    assert eliminar_subcadena_sin_rebanadas("¡Hola!",2,2)=="¡Ha!"
    assert eliminar_subcadena_con_rebanadas("¡Hola!",2,2)=="¡Ha!"
    main()