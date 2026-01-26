print ("Vamos a comprobar si has pasado de curso , dime las notas de los dos parciales que has hecho: ")
parcial1 = int(input("Nota del primer parcial: "))
parcial2 = int(input("Nota del segundo parcial: "))
notamedia = int((parcial1+parcial2)/2)
if notamedia >= 5 and (parcial1 >= 4 and parcial2 >= 4):
    print ("Has aprobado el curso")
else:
    print ("Has supendido el curso")
    if parcial1 <= 4 and parcial2 >= 5:
        print ("Tienes que recuperar el primer parcial solo")
    elif parcial2 <= 4 and parcial1 >= 5:
        print ("Tienes que recuperar el segundo parcial solo")
    elif parcial1 <= 4 and parcial2 <= 4:
        print ("Tienes que recuperar los dos parciales , no superas el 4 en ninguno de ellos")