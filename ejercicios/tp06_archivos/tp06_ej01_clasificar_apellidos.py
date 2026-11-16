def buscar_apellido(archivo,paises):

        for i in archivo:
            i = i.rstrip()
            apellido = i.strip().split(",")[0].lower()

            for letras,pais in paises.items():
                if apellido.endswith(letras):
                    try:
                        with open(pais + ".txt",'at',encoding='utf-8') as archivo:
                            archivo.write(i+ '\n')
                    except Exception as error:
                        print(error)
    
def main():

    try:
        with open ('nombres.csv','rt',encoding='utf-8') as archivo:
            paises={"ian":"ARMENIA","ini":"ITALIA","ez":"ESPAÑA"}
            buscar_apellido(archivo,paises)
    except Exception as error:
        print(error)
    else:
        print("todo correcto")

if __name__ == '__main__':

    main()