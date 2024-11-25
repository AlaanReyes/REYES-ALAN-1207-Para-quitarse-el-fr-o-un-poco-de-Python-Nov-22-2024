print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def max_in_list(numbers):
    if not numbers:  # Verificar si la lista está vacía
        return None
    
    max_num = numbers[0]  # Inicializar con el primer elemento
    for num in numbers:  # Recorrer la lista
        if num > max_num:  # Comparar cada número
            max_num = num
    return max_num

numeros = [3, 5, 7, 2, 8, 10, 4]
print("El número más grande es:", max_in_list(numeros))
