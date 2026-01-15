asignaturasycreditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignaturas, creditos in asignaturasycreditos.items():
    print ("la asignatura " , asignaturas , " tiene " , creditos)
    total_creditos = total_creditos , creditos
print ("el total de creditos es :" , total_creditos)