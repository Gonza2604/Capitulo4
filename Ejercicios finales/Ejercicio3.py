def invertir_lista(lista):
    lista_invertida = []
    
    for i in range(len(lista) - 1, -1, -1): #Recorre la lista de atras hacia adelante
        lista_invertida.append(lista[i]) #Va añadiendo cada elemento encontrado a la nueva lista
    
    return lista_invertida

numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print("Arreglo original:", numeros)
print("Arreglo invertido:", resultado)
