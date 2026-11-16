def filtrar_palabra_ciclo_normal(frase:str,num:int)->str:

    frase=frase.split(" ")
    frase_filtrada=[]
    for i in frase:
        if len(i) >= num:
            frase_filtrada.append(i)
    return " ".join(frase_filtrada)

def filtrar_palabra_listas_comprension(frase:str,num:int)->str:
    frase=frase.split(" ")
    frase_filtrada=[i for i in frase if len(i)>=num]
    return " ".join(frase_filtrada)

def main():
    num=3
    frase="El perro corre por el parque mientras los chicos juegan a la pelota y disfrutan del día"
    print(f"funcion con ciclo normal:\n{filtrar_palabra_ciclo_normal(frase,num)}")
    print(f"funcion con listas por comprension:\n{filtrar_palabra_listas_comprension(frase,num)}")

    frase_filtrada= list(filter(lambda palabra: len (palabra)>=num,frase.split(" ")))
    print(f"funcion con filter:\n{" ".join(frase_filtrada)}")

if __name__=='__main__':

    main()