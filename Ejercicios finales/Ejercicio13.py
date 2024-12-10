class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1
    
    # Verificar si la cola está vacía
    def esta_vacia(self):
        return self.frente == -1
    
    # Verificar si la cola está llena
    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente
    
    # Agregar un elemento a la cola
    def enqueue(self, elemento):
        if self.esta_llena():
            print("Error: La cola está llena.")
            return
        
        if self.esta_vacia():
            self.frente = 0
        
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = elemento
        print(f"Elemento {elemento} agregado.")
    
    # Eliminar un elemento de la cola
    def dequeue(self):
        if self.esta_vacia():
            print("Error: La cola está vacía.")
            return None
        
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        
        if self.frente == self.final:
            self.frente = self.final = -1  # Restablecer la cola si está vacía
        else:
            self.frente = (self.frente + 1) % self.capacidad
        
        print(f"Elemento {elemento} eliminado.")
        return elemento
    
    # Mostrar el estado actual de la cola
    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print("Estado actual de la cola:", self.cola)


cola = ColaCircular(5)

# Agregar elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

# Intentar agregar más elementos
cola.enqueue(60)

# Mostrar la cola
cola.mostrar_cola()

# Eliminar algunos elementos
cola.dequeue()
cola.dequeue()

# Mostrar la cola después de eliminar
cola.mostrar_cola()

# Agregar más elementos después de eliminar
cola.enqueue(60)
cola.enqueue(70)

# Mostrar la cola final
cola.mostrar_cola()
