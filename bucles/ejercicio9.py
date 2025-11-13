contraseña = "contraseña"
intento = input("Cual es la contraseña? :")
while True:
    if intento == contraseña:
        print ("La contraseña es correcta")
        break
    else:
        intento=input("Esa no es la contraseña , vuelve a intentarlo: ")