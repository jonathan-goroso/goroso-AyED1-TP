
def eliminar_subcadena_con_rebanadas(frase:str,comienzo:int)->str:
    frase_filtrada=frase[-(comienzo):]
    return frase_filtrada

def main():

    frase="El perro corre por el parque mientras los chicos juegan a la pelota y disfrutan del día"
    ultimos=17
    print(f"{frase}\nultimos {ultimos} caracteres:\n{eliminar_subcadena_con_rebanadas(frase,ultimos)}")

if __name__=='__main__':

    main()