class Cola:
    def __init__(self):
        self.elementos = []
    
    # Agregar un elemento al final de la cola
    def enqueue(self, elemento):
        self.elementos.append(elemento)
    
    # Eliminar el primer elemento de la cola
    def dequeue(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    
    # Ver el primer elemento de la cola
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None
    
    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.elementos) == 0


cola = Cola()

cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")

print(f"Primer elemento (peek): {cola.peek()}")

# Eliminar elementos
print(f"Elemento eliminado: {cola.dequeue()}")
print(f"Elemento eliminado: {cola.dequeue()}")

# Ver el siguiente elemento
print(f"Primer elemento (peek): {cola.peek()}")

# Eliminar el último elemento
print(f"Elemento eliminado: {cola.dequeue()}")

# Verificar si está vacía
print(f"¿Está vacía? {cola.esta_vacia()}")
