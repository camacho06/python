productos = input("Ingrese los nombres de los productos separados por comas: ")
lista_productos = productos.split(",")
for producto in lista_productos:
    print("Producto: " + producto.strip())