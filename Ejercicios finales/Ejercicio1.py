numeros = [1, 2, 3, 4, 5] #Se define la lista

suma = 0 #Esta variable almacenará los números que se vayan sumando, se inicia en cero porque no se ha comenzado a sumar

for numero in numeros: #Se inicia el bucle que pasará por toda la lista, siendo "numero" la variable que tomará el valor de cada elemento nuevo
    suma += numero #Se le va sumando cada elemento a la variable "suma"

print("La suma de los números es:", suma)