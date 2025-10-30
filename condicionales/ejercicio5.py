edadminima = 16
ingresosminimos = 1000
edad = int(input("Ingrese su edad: "))
ingresosmensuales = float(input("Ingrese sus ingresos mensuales: "))
if edadminima < edad and ingresosmensuales >= ingresosminimos:
    print("Si tributa.")
else:
    print("No tributa.")