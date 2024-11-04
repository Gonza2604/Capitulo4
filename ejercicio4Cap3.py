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

        write_index = 1
        for i in range(1, len(self.data)):
            if self.data[i] != self.data[i - 1]:
                self.data[write_index] = self.data[i]
                write_index += 1
        self.data = self.data[:write_index]
        return self.data

    def mediana(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_data[n // 2]

    def odd_even_sort(self):
        n = len(self.data)
        is_sorted = False
        pass_count = 0  # Contador de pasadas

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
            
            pass_count += 1  # Incrementar el contador de pasadas

        return pass_count  # Devolver el número de pasadas realizadas

if __name__ == "__main__":
    arr = Array([5, 3, 8, 6, 2, 7, 4, 1])
    print("Array original:", arr.data)
    passes = arr.odd_even_sort()
    print("Array ordenado:", arr.data)
    print("Número de pasadas:", passes)
