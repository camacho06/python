dic = {'platano':1.35 , 'manzana':0.80 , 'pera':0.85 , 'naranja':0.70}
fruta = input("Cual es la fruta que deseas?: ")

if fruta in dic:
    kilos = int(input("dime cuantos kilos quieres: "))
    print ("este es el precio de la fruta que seleccionaste " + dic[fruta] + "€")
    total = dic[fruta] * kilos
    print ("este es el precio final para los kilos que querias: " + total)
else:
    print ("No se encuentra la fruta ")