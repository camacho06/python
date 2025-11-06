sexo = input("Ingrese su sexo (M/F): ").upper()
nombre = input("Ingrese su nombre: ")
inicial = nombre[0].lower()
if sexo == "M" and inicial > "n": 
    print(f"{nombre} pertenece al grupo A.")
elif sexo == "F" and inicial < "n":
    print(f"{nombre} pertenece al grupo A.")
else:
    print(f"{nombre} pertenece al grupo B.")