cantidadinvertir=float(input("Ingrese la cantidad a invertir: "))
interesanual=float(input("Ingrese el interes anual (en porcentaje): "))
años=int(input("Ingrese el numero de años: "))
capital=cantidadinvertir*((interesanual/100)+1)**años
print("El capital final despues de " + str(años) + " años es: " + str(capital))