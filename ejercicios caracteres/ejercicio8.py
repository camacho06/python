precioproducto=input("Ingrese el precio del producto en euros con dos decimales: ")
x = precioproducto.split(".")
print("El precio del producto sin decimales es: " + x[0] + " euros")
print("Los decimales del precio del producto son: " + x[1] + " centimos")