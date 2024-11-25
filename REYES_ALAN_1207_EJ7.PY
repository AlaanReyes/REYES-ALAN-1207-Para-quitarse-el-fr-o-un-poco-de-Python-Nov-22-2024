print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO
# Pedir al usuario que ingrese 10 edades
edades = tuple(int(input(f"Ingrese la edad de la persona {i + 1}: ")) for i in range(10))

# Contar las edades mayores a 20
mayores_20 = sum(1 for edad in edades if edad > 20)

print(f"La cantidad de personas con edades mayores a 20 es: {mayores_20}")
