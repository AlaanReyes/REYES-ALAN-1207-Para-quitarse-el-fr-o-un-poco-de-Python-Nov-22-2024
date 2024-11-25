print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():  # Verifica si el carácter es una letra mayúscula
            contador += 1
    return contador

# Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Por favor, ingresa una cadena: ")
cantidad_mayusculas = contar_mayusculas(cadena_usuario)

print(f"La cadena ingresada tiene {cantidad_mayusculas} letra(s) mayúscula(s).")
