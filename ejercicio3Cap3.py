class Array:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def deduplicate(self):
        if not self.data:
            return []

        # Utilizamos un índice para escribir los elementos únicos
        write_index = 1

        for i in range(1, len(self.data)):
            if self.data[i] != self.data[i - 1]:  # Solo copiar si es diferente del anterior
                self.data[write_index] = self.data[i]
                write_index += 1

        # Recortamos la lista para que contenga solo elementos únicos
        self.data = self.data[:write_index]
        return self.data

    def mediana(self):
        sorted_data = sorted(self.data)  # Ordenar la lista
        n = len(sorted_data)
        
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_data[n // 2]

# Ejemplo de uso
if __name__ == "__main__":
    arr = Array([1, 1, 2, 2, 3, 4, 4, 5, 5])
    arr.bubble_sort()
    print("Array ordenado:", arr.data)
    unique_array = arr.deduplicate()
    print("Array sin duplicados:", unique_array)
    print("Mediana:", arr.mediana())
