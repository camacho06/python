print ("Bienvenido al menu de camacho, puedo hacer lo siguiente: ")
print ("1. Añadir numero a la lista \
2. Añadir numero de la lista en una posicion \
3. Longitud de la lista \
4. Eliminar el ultimo numero \
5. Eliminar un numero \
6. Contar numeros \
7. Posicion de un numero \
8. Mostrar numeros \
9. Salir ")
while True:
    lista=[]
    accion = input("Dime que quieres hacer , dame una accion (1 al 9): ")
    if accion == "1":
        numero=str(input("Que numero quieres añadir? : "))
        lista.append(numero)
    elif accion == "2":
        numero=str(input("Que numero quieres añadir? : "))
        posicion=input("En que posicion quieres poner el numero?: ")
        lista.append(numero)
    elif accion == "3":
        longitud=len(lista)
        print(longitud)
    elif accion == "8":
        for i in lista:
            print(i, end=" ")
    elif accion == "9":
        break
    else:
        print ("Accion incorrecta intentelo de nuevo")