def analizar_frase(frase):

    palabras = frase.split()
    contarpalabras = {}
    repetidas = []

    for p in palabras:
        if p in contarpalabras:
            contarpalabras[p] += 1
        else:
            contarpalabras[p] = 1
    for palabra, cuenta in contarpalabras.items():
        if cuenta > 1:
            repetidas.append(palabra)
    return contarpalabras, repetidas

texto = "La caracola está enterrada al lado de otra caracola de color"
diccionario, listaRepetidas = analizar_frase(texto)

print(f"Diccionario: {diccionario}")
print(f"Repetidas: {listaRepetidas}")