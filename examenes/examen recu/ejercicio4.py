print ("Bienvenido al menu de camacho, puedo hacer lo siguiente: ")
print ("1. Contar palabras de una frase \
2. Mostrar las palabras de una frase en líneas distintas \
3. Mostrar la frase con todas sus letras en mayúsculas \
4. Salir del programa")
while True:
    accion = input("Dime que quieres hacer , dame una accion (1 al 4): ")
    if accion == "1":
        frase = input("Dame una frase: ")
        print (len(frase.split()))
    elif accion == "2":
        frase = input("Dame una frase: ")
        palabras = frase.split()
        for i in palabras :
            print (i)
    elif accion == "3":
        frase = input("Dame una frase: ")
        print (frase.upper())
    elif accion == "4":
        break
    else:
        print ("Accion incorrecta intentelo de nuevo")