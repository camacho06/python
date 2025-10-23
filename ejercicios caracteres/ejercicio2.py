nombre=input("Ingrese su nombre : ")
apellido1=input("Ingrese su primer apellido : ")
apellido2=input("Ingrese su segundo apellido : ")
nombrecompleto= nombre + " " + apellido1 + " " + apellido2
print("Su nombre completo es: " + nombrecompleto)
print("Su nombre completo en mayusculas es: " + nombrecompleto.upper())
print("Su nombre completo en minusculas es: " + nombrecompleto.lower())
print("Su nombre completo con la primera letra en mayuscula es: " + nombre.capitalize() + " " + apellido1.capitalize() + " " + apellido2.capitalize())