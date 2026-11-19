class menorCeroError(Exception):
    pass

def mcd(x: int, y: int) -> int:
    if x == y:
        return x
    elif x > y:
        return mcd(x - y, y)
    else:
        return mcd(y, x)


def mcd_lista(lista: list[int]) -> int:
    if len(lista) == 1:
        return lista[0]

    return mcd(mcd_lista(lista[:-1]), lista[-1])


def main():

    nums= (12,8)
    numeros=[12,8,16]
    try:
        if nums[0]<0 or nums[1]<0:
            raise menorCeroError()
    except menorCeroError:
        print("no se permiten numeros menores a 0")
    else:
        print(mcd(nums[0],nums[1]))
        print(mcd_lista(numeros))


if __name__ == '__main__':

    main()