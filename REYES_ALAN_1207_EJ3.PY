print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def filtrar_palabras(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]

lista_palabras = ["gato", "elefante", "murcielago", "jirafa", "sol"]
n = 5
print("Palabras con más de", n, "caracteres:", filtrar_palabras(lista_palabras, n))
