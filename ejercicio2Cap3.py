class Array:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def mediana(self):
        # Ordenamos los elementos
        sorted_data = sorted(self.data)  # Ordenar la matriz
        n = len(sorted_data)
        
        # Calcular la mediana
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2  # Promedio de los dos del medio
        else:
            return sorted_data[n // 2]  # Elemento del medio

if __name__ == "__main__":
    arr = Array([3, 1, 7, 4, 8, 5, 9, 2, 6])
    arr.bubble_sort()
    print("Array ordenado:", arr.data)
    print("Mediana:", arr.mediana())
