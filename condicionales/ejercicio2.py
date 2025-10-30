contraseña = "contraseña"
ingresada = input("Ingrese la contraseña: ")
ingresada = ingresada.lower()
if ingresada == contraseña:
    print("Acceso concedido.")
else:
    print("contraseña incorrecta. Acceso denegado.")