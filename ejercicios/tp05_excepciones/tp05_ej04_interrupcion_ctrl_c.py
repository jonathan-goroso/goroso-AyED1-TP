def main():
    for i in range(100000):
        try:
            print(i)
        
        except KeyboardInterrupt:
            decicion=(input(f"ingrese si para confirmar la interrupcion: ")).lower()
            if decicion=="si":
                break


if __name__=='__main__':

    main()