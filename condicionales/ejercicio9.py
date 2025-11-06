edad=int(input("Cuantos años tienes?: "))
if edad < 4:
    print("Tu entrada es gratuita")
elif edad > 4 and edad < 18:
    print("Tu entrada tiene un coste de 5€ ")
else:
    print("Tu entrada tiene un coste de 10€ ")