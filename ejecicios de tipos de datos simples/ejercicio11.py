cantidaddepositadacuentadeahorros=float(input("Ingrese la cantidad depositada en la cuenta de ahorros: "))
interesanual=0.04
cantidaddeahorros1año=cantidaddepositadacuentadeahorros*interesanual
print("La cantidad de ahorros en un año es: " + str(cantidaddeahorros1año) + " euros")
cantidaddeahorros2años=(cantidaddepositadacuentadeahorros+cantidaddeahorros1año)*interesanual
print("La cantidad de ahorros en dos años es: " + str(cantidaddeahorros2años) + " euros")
cantidaddeahorros3años=(cantidaddepositadacuentadeahorros+cantidaddeahorros1año+cantidaddeahorros2años)*interesanual
print("La cantidad de ahorros en tres años es: " + str(cantidaddeahorros3años) + " euros")