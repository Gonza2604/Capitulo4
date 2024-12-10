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
    
    def mostrar_cola(self):
        print("Cola:", self.elementos)


def reorganizar_pares_impares(cola):
    pares = Cola()
    impares = Cola()
    
    # Clasificar elementos
    while not cola.esta_vacia():
        numero = cola.dequeue()
        if numero % 2 == 0:
            pares.enqueue(numero)
        else:
            impares.enqueue(numero)
    
    # Combinar pares e impares en la cola original
    while not pares.esta_vacia():
        cola.enqueue(pares.dequeue())
    
    while not impares.esta_vacia():
        cola.enqueue(impares.dequeue())


cola = Cola()

numeros = [3, 8, 5, 2, 9, 6, 7, 4, 1]
for num in numeros:
    cola.enqueue(num)

print("Antes de reorganizar:")
cola.mostrar_cola()

# Reorganizar la cola
reorganizar_pares_impares(cola)

print("Después de reorganizar:")
cola.mostrar_cola()
