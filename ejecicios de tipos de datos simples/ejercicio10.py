cantidadpayasospedido=float(input("Ingrese la cantidad de payasos pedidos: "))
cantidadmuñecaspedido=float(input("Ingrese la cantidad de muñecas pedidos: "))
pesopayaso=112
pesomuñeca=75
pesototal=(cantidadpayasospedido*pesopayaso)+(cantidadmuñecaspedido*pesomuñeca)
print("El peso total del pedido es: " + str(pesototal) + " gramos")