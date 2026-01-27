lista = [50, 4, 28, 33, 12]
suma = 0
while True:
    print ("SUMAR Y GANAR Vaya sumando todos los números que le iré diciendo. Empezamos por 0")
    for numero in lista:
        suma = suma + numero
        print ("Mas ", numero)
        intento = input("Cuanto es?: ")
        if suma != intento:
            print ("Fallaste respuesta incorrecta")
            break
    print ("Acabaste todos los numeros , ENHORABUENA")