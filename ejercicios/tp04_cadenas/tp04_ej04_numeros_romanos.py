def convertir_romano(num:int)->str:
    """
    recibe un numero y lo convierte en un numero romano
    pre:recibe como parametro un entero entre 0 y 3999
    post:devuelve un string
    """
    romano=[]
    num_romanos={"M":1000,"D":500,"CD":400,"C":100,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}
    for key, valor in num_romanos.items():
        while True:
            if valor<= num:
                num-=valor
                romano.append(key)
            else:
                break
    return "".join(romano)

def main():
    num=11
    print(convertir_romano(num))

if __name__== '__main__':

    main()