Lista = [3, 7, 1, 9, 4]
numero_a_buscar = int(input("Introduce el número que deseas buscar: ")) #Le pide al usuario ingresar una variable de tipo entero

#Variable para indicar si el número fue encontrado
Encontrado = False  # Inicialmente asumimos que no está

for numero in Lista:
    if numero == numero_a_buscar:
        Encontrado = True
        break  # Salimos del bucle porque ya lo encontramos

if Encontrado:
    print(f"El número {numero_a_buscar} está presente en el arreglo.")
else:
    print(f"El número {numero_a_buscar} NO está presente en el arreglo.")