print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def calcular_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento

# Solicitar el año en curso
anio_actual = int(input("Ingresa el anio en curso: "))

# Solicitar el nombre y anio de nacimiento de tres personas
personas = []
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    anio_nacimiento = int(input(f"Ingrese el anio de nacimiento de {nombre}: "))
    personas.append((nombre, anio_nacimiento))

# Calcular y mostrar las edades
print("\nEdades durante el anio en curso:")
for nombre, anio_nacimiento in personas:
    edad = calcular_edad(anio_actual, anio_nacimiento)
    print(f"{nombre} cumplira {edad} anios en el anio {anio_actual}.")
