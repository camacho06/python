dic = {'euro':'€', 'dollar':'$', 'yen':'¥'}
divisa = input("Cual es la divisa?: ")

if divisa in dic:
    print (dic[divisa])
else:
    print ("No se encuentra la divisa")