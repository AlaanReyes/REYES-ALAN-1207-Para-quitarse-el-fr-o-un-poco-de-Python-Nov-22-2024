print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def mas_larga(palabras):
    if not palabras:  # Verificar si la lista está vacía
        return None

    palabra_larga = palabras[0]  # Inicializar con la primera palabra
    for palabra in palabras:  # Recorrer la lista
        if len(palabra) > len(palabra_larga):  # Comparar las longitudes
            palabra_larga = palabra
    return palabra_larga

lista_palabras = ["gato", "elefante", "murcielago", "jirafa"]
print("La palabra más larga es:", mas_larga(lista_palabras))
