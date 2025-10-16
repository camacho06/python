preciobarrapan=3,49
numerobarrascompradas=int(input("Ingrese el numero de barras compradas que no son del dia: "))
print("el precio habitual de una barra de pan es: " + str(preciobarrapan) + " euros")
descuento=preciobarrapan*0.6
print("el descuento por barra de pan que no es del dia es: " + str(descuento) + " euros")
preciobarrapanconeldescuento=preciobarrapan-descuento
print("el precio de una barra de pan con el descuento aplicado es: " + str(preciobarrapanconeldescuento) + " euros")