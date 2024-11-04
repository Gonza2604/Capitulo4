class Array:
    def __init__(self, data):
        self.data = data

    def insertion_sort(self):
        n = len(self.data)
        comparisons = 0
        copies = 0
        
        for i in range(1, n):
            key = self.data[i]
            j = i - 1

            # Comparaciones en el bucle while
            while j >= 0 and self.data[j] > key:
                comparisons += 1  # Contar la comparación
                self.data[j + 1] = self.data[j]
                copies += 1  # Contar la copia
                j -= 1
            
            # Si la comparación falla, cuenta esa comparación también
            if j >= 0:
                comparisons += 1  # Contar la comparación que falló
            
            self.data[j + 1] = key
            copies += 1  # Contar la copia del key

        print(f"Comparaciones: {comparisons}, Copias: {copies}")

    def odd_even_sort(self):
        n = len(self.data)
        is_sorted = False
        pass_count = 0

        while not is_sorted:
            is_sorted = True
            
            # Pasada impar
            for j in range(1, n - 1, 2):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    is_sorted = False
            
            # Pasada par
            for j in range(0, n - 1, 2):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    is_sorted = False
            
            pass_count += 1

        return pass_count

if __name__ == "__main__":
    # Datos ordenados inversamente
    reverse_sorted_array = Array(list(range(10, 0, -1)))
    print("Array original (inversamente ordenado):", reverse_sorted_array.data)
    reverse_sorted_array.insertion_sort()
    print("Array ordenado:", reverse_sorted_array.data)

    # Datos casi ordenados
    almost_sorted_array = Array([1, 2, 3, 5, 4, 6, 7, 8, 9, 10])
    print("\nArray original (casi ordenado):", almost_sorted_array.data)
    almost_sorted_array.insertion_sort()
    print("Array ordenado:", almost_sorted_array.data)
