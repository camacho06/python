pizza = input("Quieres una pizza vegetariana o una normal? ").lower
if pizza == "vegetariana":
    print("Los ingredientes de una pizza de perrosflautas vegetarianos son:" \
    " Pimiento y tofu")
    ingrediente = input("Introduce tu ingrediente a elegir")
else:
    print("Los ingredientes de una pizza normal son: " \
    " Peperoni, Jamón y Salmón")
    ingrediente = input("Introduce tu ingrediente a elegir")
print("Su pizza es " ) + pizza + " y lleva " + ingrediente