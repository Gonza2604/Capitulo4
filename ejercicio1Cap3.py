def bidirectional_bubble_sort(arr):
    n = len(arr)
    izquierda = 0
    derecha = n - 1

    while izquierda < derecha:
        # Desplazamiento de izquierda a derecha
        for i in range(izquierda, derecha):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        # Después del primer recorrido, decrementar el índice derecho
        derecha -= 1
        
        # Desplazamiento de derecha a izquierda
        for i in range(derecha, izquierda, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        
        # Después del segundo recorrido, incrementar el índice izquierdo
        izquierda += 1

    return arr

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bidirectional_bubble_sort(array)
print("Array ordenado:", sorted_array)
