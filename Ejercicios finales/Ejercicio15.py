class Cola:
    def __init__(self):
        self.elementos = []
    
    def enqueue(self, elemento):
        self.elementos.append(elemento)
    
    def dequeue(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def tamano(self):
        return len(self.elementos)
    
    def mostrar_cola(self):
        print("Cola:", self.elementos)


# Función para encontrar y eliminar el valor mínimo en la cola
def encontrar_y_eliminar_minimo(cola, tamano):
    minimo = float('inf')
    contador = 0
    
    # Encontrar el mínimo
    for _ in range(tamano):
        valor = cola.dequeue()
        if valor < minimo:
            minimo = valor
        cola.enqueue(valor)
    
    # Eliminar una sola vez el mínimo
    for _ in range(tamano):
        valor = cola.dequeue()
        if valor == minimo and contador == 0:
            contador += 1  # Eliminar solo la primera ocurrencia
        else:
            cola.enqueue(valor)
    
    return minimo


# Función para ordenar la cola
def ordenar_cola(cola):
    cola_ordenada = Cola()
    
    while not cola.esta_vacia():
        tamano_actual = cola.tamano()
        minimo = encontrar_y_eliminar_minimo(cola, tamano_actual)
        cola_ordenada.enqueue(minimo)
    
    return cola_ordenada


cola = Cola()
numeros = [5, 3, 8, 1, 4, 7, 2, 6]
for num in numeros:
    cola.enqueue(num)

print("Antes de ordenar:")
cola.mostrar_cola()

# Ordenar la cola
cola_ordenada = ordenar_cola(cola)

print("Después de ordenar:")
cola_ordenada.mostrar_cola()
