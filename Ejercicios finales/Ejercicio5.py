def eliminar_duplicados(arreglo):
    Lista_unicos = []
    
    for elemento in arreglo:
        if elemento not in Lista_unicos: #Verifica si el elemento ya está en el nuevo arreglo
            Lista_unicos.append(elemento)  # Si no está, lo añadimos
    
    return Lista_unicos

Lista = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(Lista)
print("Arreglo original:", Lista)
print("Arreglo sin duplicados:", resultado)
