def binario_a_decimal(binario: str) -> int:
    if len(binario) == 1:
        return int(binario)

    return binario_a_decimal(binario[:-1]) * 2 + int(binario[-1])


def main():

    binario = "1111"
    print(binario_a_decimal(binario))


if __name__ == "__main__":

    main()
