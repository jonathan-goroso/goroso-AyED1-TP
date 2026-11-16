def extraer_subcadena_sin_rebanadas(frase:str,comienzo:int,caracteres:int)->str:

    frase_filtrada=[frase[i] for i in range(comienzo,comienzo+caracteres) if i< len(frase)]
    return "".join(frase_filtrada)

def extraer_subcadena_con_rebanadas(frase:str,comienzo:int,caracteres:int)->str:
    frase_filtrada=frase[comienzo:comienzo+caracteres]
    return frase_filtrada

def main():

    frase="El perro corre por el parque mientras los chicos juegan a la pelota y disfrutan del día"
    comienzo=38
    caracteres=29
    print(f"funcion sin rebanadas: \n{extraer_subcadena_sin_rebanadas(frase,comienzo,caracteres)}")
    print(f"funcion con rebanas:\n{extraer_subcadena_con_rebanadas(frase,comienzo,caracteres)}")

if __name__=='__main__':

    assert extraer_subcadena_sin_rebanadas("hola",2,2)=="la"
    assert extraer_subcadena_con_rebanadas("hola",2,2)=="la"
    main()