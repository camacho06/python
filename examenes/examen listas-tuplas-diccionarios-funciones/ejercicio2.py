saldo = 0
# operaciones = []
while 0 < 1:
    accion = input("Que desea realizar " \
    "1- ingreso " \
    "o " \
    "2- reintegro" \
    "cualquier otra para salir: ")
    if accion == "1":
        cantidad = int(input("Cuanto quieres ingresar?: "))
        saldo = saldo + cantidad
        operaciones = cantidad
    elif accion == "2":
        cantidad = int(input("Cuanto quieres sacar?: "))
        if cantidad > saldo:
            print ("Imposible realizar el reintegro , causa: saldo insuficiente")
        else:
            saldo = saldo - cantidad
    else:

        break
    print ("Tienes esta cantidad en tu saldo :" , saldo )
    #print (operaciones)