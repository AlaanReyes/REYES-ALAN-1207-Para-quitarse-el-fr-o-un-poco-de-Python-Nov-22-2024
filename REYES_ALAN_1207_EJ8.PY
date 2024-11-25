print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO
# Lista de nombres
nombres = ["Ana", "Alberto", "Beatriz", "Carlos", "Andrea", "Diana", "Alan"]

# Solicitar al usuario la letra a buscar
letra = input("Ingrese la letra por la que deben comenzar los nombres: ").lower()

# Contar los nombres que comienzan con la letra elegida
cantidad = sum(1 for nombre in nombres if nombre.lower().startswith(letra))

print(f"La cantidad de nombres que comienzan con la letra '{letra}' es: {cantidad}")
