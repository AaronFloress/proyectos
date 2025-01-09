#calculadora de consola

print("---BIENVENIDO---")

while True:

    n1= float(input("Ingresa el primer numero: "))
    n2= float(input("Ingresa el segundo numero: "))

    def suma():
        resultado=n1+n2
        print(f"el resultado de la suma es: {resultado}")

    def resta():
        resultado=n1-n2
        print(f"el resultado de la resta es: {resultado}")

    def multi():
        resultado=n1*n2
        print(f"el resultado de la multiplicación es: {resultado}")

    def division():
        resultado=n1/n2
        print(f"el resultado de la division es: {resultado}")

    def exp():
        resultado=n1**n2
        print(f"el resultado de la operación es: {resultado}")


    opc=int(input("Elige una opcion: \n1) Suma\n2) Resta\n3) Multiplicación\n4) División\n5) Exponente\n6) Salir\n"))


    if opc==1:
        suma()

    elif opc==2:
        resta()

    elif opc==3:
        multi()

    elif opc==4:
        division()

    elif opc==5:
        exp()

    elif opc==6:
        print("saliste de la calculadora :(")
        exit()

    else:
        print("elige una opcion correcta")

