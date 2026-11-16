def main():

    claveMaestra=123456789
    impar=True
    clave1=[]
    clave2=[]
    for i in str(claveMaestra):
        if impar:
            clave1.append(i)
            impar = False
        else:
            clave2.append(i)
            impar = True

    print(f"la clave 1 es: {"".join(clave1)}")
    print(f"la clave 2 es: {"".join(clave2)}")

if __name__=='__main__':

    main()