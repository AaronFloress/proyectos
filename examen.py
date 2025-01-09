count=0

print("10 Preguntas cultura general")
print("si obtienes 60 puntos o mas pasas a la siguiente ronda!!!")

while True:
    print("pregunta numero 1:")
    opc=int(input("¿PI tiene un valor de 3.1417?\n1) Si \n2) No\n"))
    if opc==2:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero :2")
    opc=int(input("¿El cubo rubik 3x3 tiene 6 centros?\n1) Si \n2) No\n"))
    if opc==1:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 3:")
    opc=input("¿En que continente esta México?\n") 
    opc=opc.upper()
    if opc=="AMERICA":
        print("✅")
        count=count+10
        print(count)
    else:
        print("❌")

    print("pregunta numero 4:")
    opc=int(input("¿cuanto es 8+2x4?\n"))
    if opc==16:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 5:")
    opc=int(input("Que se celebra el 10 de mayo?\n 1) Dia de las madres\n 2) Dia de la independencia\n 3) Nada"))
    if opc==1:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 6:")
    opc=int(input("¿cuantas cuerdas tiene una guitarra?\n"))
    if opc==6:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 7:")
    opc=int(input("¿cuantas cuerdas tiene un bajo?\n"))
    if opc==4:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 8:")
    opc=int(input("¿cuantos años dura la primaria?\n"))
    if opc==6:
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 9:")
    opc=input("¿cual es la materia mas innecesaria que se da en las escuelas?\n"+"\x1b[1;31m pista: etica\n"+"\x1b[1;31m")
    opc=opc.upper()
    if opc=="ETICA":
        print("✅")
        count=count+10
    else:
        print("❌")

    print("pregunta numero 10:")
    opc=int(input("¿cuantas semanas tiene un año?\n"))
    if opc==52:
        print("✅")
        count=count+10
    else:
        print("❌")

    if count>60:
        print(f"felicidades, pasaste a la siguiente ronda con un puntaje de: {count}pts")

    opc=input("quieres seguir jugando o pasar a la siguiente ronda?")
    if opc=="no":
        break

    



