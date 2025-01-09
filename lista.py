#lista de tareas con conexion a base de datos con mysql que permite ver la lista, agregar y eliminar
import pymysql

Connection = pymysql.connect(
    host="localhost",
    passwd="12345678",
    user="root",
    db="tasks"
)
cur = Connection.cursor()

# Recorrer la lista de tareas y enumerarlas
def showlist():
    print("--------------------------")
    cur.execute("SELECT pending FROM list")
    pending=cur.fetchall()
    for i, (task,) in enumerate(pending, start=1):
        print(f"{i} {task}")
    print("--------------------------")

#agrega a la lista
def add():
    print("--------------------------")
    addlist = input("Ingresa lo que deseas agregar: ")
    addlist=addlist.upper()
    cur.execute("INSERT INTO list (pending) VALUES (%s)", (addlist,))
    Connection.commit()  # Confirmar los cambios en la base de datos
    print("Tarea agregada exitosamente.")
    print("--------------------------")

#elimina de la lista en la DB
def dele():

    showlist()
    dele=input(f"escribe que tarea deseas remover: ").upper()
    cur.execute("DELETE FROM list WHERE TRIM(pending) = %s", (dele,))
    Connection.commit() #confirmar la eliminacion
    print("Tarea eliminada exitosamente")
    print("--------------------------")

while True:

    opc=int(input("selecciona alguna de las siguientes opciones: \n1) Lista \n2) Agregar \n3) Eliminar \n4) Salir\n---------------------------------------------\n"))

    if opc==1:
        showlist()
    elif opc==2:
        add()
    elif opc==3:
        dele()
    elif opc==4:
        print("Saliste!")
        break
    else:
        break

# Cerrar la conexión después de todas las operaciones
cur.close()
Connection.close()