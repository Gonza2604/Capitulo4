numeros = [3, 1, 7, -2, 10, 5]

maximo = numeros[0]  # Asumimos que el primer número es el más grande
minimo = numeros[0]  # Asumimos que el primer número es el más pequeño

for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)