altura=int(input("altura de la diagonal inversa: "))
espacios=altura-1
while altura != 0:
    print(" "*espacios+"*")
    espacios=espacios-1
    altura=altura-1