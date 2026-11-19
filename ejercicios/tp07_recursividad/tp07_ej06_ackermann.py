import sys


def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def main():

    sys.setrecursionlimit(1025)
    print(" m/n |", end=" ")

    for n in range(8):
        print(f"{n:5}", end="")

    print()
    print("-" * 47)

    for m in range(4):
        print(f"{m:4} |", end="")

        for n in range(8):
            print(f"{ackermann(m, n):5}", end="")

        print()


if __name__ == "__main__":
    main()
