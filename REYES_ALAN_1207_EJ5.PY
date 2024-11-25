print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def binario_a_entero(binario):
    try:
        return int(binario, 2)  # Convierte el numero binario a entero
    except ValueError:
        return "Entrada no válida. Asegúrate de ingresar solo dígitos binarios (0 y 1)."

# Solicitar al usuario que ingrese un numero binario
binario_usuario = input("Ingresa un numero binario: ")
entero = binario_a_entero(binario_usuario)

print(f"El número binario {binario_usuario} convertido a entero es: {entero}")
