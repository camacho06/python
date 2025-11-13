numero=int(input("Introduce un numero entero positivo: "))
temp=1
contador=0
while temp<=numero:
    if numero%temp == 0 :
        contador+=1
    temp+=1
if contador == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")