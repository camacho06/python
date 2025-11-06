renta = float(input("Introduce tu renta anual en euros: "))
if renta < 10000:
    tipo_impositivo = 5
elif renta < 20000 and renta >= 10000:
    tipo_impositivo = 15
elif renta < 35000 and renta >= 20000:
    tipo_impositivo = 20
elif renta < 60000 and renta >= 35000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45