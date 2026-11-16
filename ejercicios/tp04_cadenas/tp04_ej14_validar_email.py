import re


def validar_mail(mail):

    patron_mail = r"[A-Za-z0-9]+@[A-Za-z0-9]+(.com|.com.ar)"

    return bool(re.fullmatch(patron_mail, mail))


def main():

    dominios = []
    while True:

        mail = input("ingrese un mail: ")

        if mail == "":
            break
        elif validar_mail(mail):
            dominio = mail.split("@")[1].casefold()
            if dominio not in dominios:
                dominios.append(dominio)
        else:
            print("mail invalido")
    dominios.sort()

    print("los dominios son:")
    for i in dominios:
        print(i)


if __name__ == "__main__":

    main()
