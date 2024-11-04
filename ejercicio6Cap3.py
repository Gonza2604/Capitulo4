class Array:
    def __init__(self, data):
        self.data = data

    def insertion_sort_and_dedupe(self):
        n = len(self.data)
        special_value = float('-inf')  # Valor especial para marcar duplicados
        duplicate_count = 0  # Contador de duplicados

        for i in range(1, n):
            key = self.data[i]
            j = i - 1

            # Mover los elementos mayores que 'key' a una posición adelante
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1

            # Comprobar si el valor ya existe en la parte ordenada
            if j >= 0 and self.data[j] == key:
                # Encontramos un duplicado
                duplicate_count += 1
                self.data[i] = special_value  # Marcar el duplicado
            else:
                # Colocar el valor único en su lugar
                self.data[j + 1] = key

        # Segunda pasada para mover las claves únicas a sus posiciones
        unique_index = 0
        for k in range(n):
            if self.data[k] != special_value:
                self.data[unique_index] = self.data[k]
                unique_index += 1

        # Recortar el array para que contenga solo elementos únicos
        self.data = self.data[:unique_index]

        print(f"Elementos únicos: {self.data}")

    def insertion_sort(self):
        n = len(self.data)
        comparisons = 0
        copies = 0
        
        for i in range(1, n):
            key = self.data[i]
            j = i - 1

            while j >= 0 and self.data[j] > key:
                comparisons += 1
                self.data[j + 1] = self.data[j]
                copies += 1
                j -= 1
            
            if j >= 0:
                comparisons += 1
            
            self.data[j + 1] = key
            copies += 1

        print(f"Comparaciones: {comparisons}, Copias: {copies}")

if __name__ == "__main__":
    # Datos con duplicados
    array_with_duplicates = Array([5, 3, 8, 5, 2, 3, 7, 8, 1])
    print("Array original con duplicados:", array_with_duplicates.data)
    array_with_duplicates.insertion_sort_and_dedupe()
    print("Array después de ordenar y eliminar duplicados:", array_with_duplicates.data)
