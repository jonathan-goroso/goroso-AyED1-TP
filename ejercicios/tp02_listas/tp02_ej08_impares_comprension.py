def main():
    
    #genera una lista con todos los números impares comprendidos entre 100 y 200
    num_impares=[n for n in range(100,201) if n %2]

    print(num_impares)

if __name__=='__main__':
    main()