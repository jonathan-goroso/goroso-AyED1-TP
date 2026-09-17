def main():

    lista1=[1,3,5,7,9]
    lista2=[2,4,6,8,10,12]

    num=0
    
    for i in range(1,len(lista2)*2,2):

        lista1[i:i]=lista2[num:num+1]
        num+=1

    print(lista1)

if __name__=='__main__':

    main()