palabras = "HOLA MUNDO hola MUNDO hola mundo"
palabras = palabras.lower()
palabras = palabras.split(" ")
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
        print(diccionario_frecuencias[palabra])
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' se repite {frecuencia} veces")