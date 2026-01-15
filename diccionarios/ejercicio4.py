meses = {'01':'Enero', '02':'Febrero', '03':'Marzo', '04':'Abril', '05':'Mayo', '06':'Junio', '07':'Julio', '08':'Agosto', '09':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}
fecha = input("introduce la fecha de hoy con el siguiente formato dd/mm/aaaa: ")
dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
año = fecha.split("/")[2]
print ("Hoy es " + dia + " de " + meses[mes] + " del " + año)