class CeroError(Exception):
    pass

def ingresar_numero() -> int:
    numero = 0
    try:
        numero = int(input('Ingrese un número: '))
        if numero <= 0:
            raise CeroError()

    except ValueError:
        print("Debe ingresar un número entero")

    except CeroError:
        print('No puede ser menor o igual a 0')

    finally:
        return numero

def main():
    num = ingresar_numero()
    if num:
        print(num)

if __name__ == '__main__':
    main()
