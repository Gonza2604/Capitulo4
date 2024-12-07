class Pila:
    def __init__(self):
        #Inicializa una pila vacía
        self.elementos = []
    
    def push(self, elemento):
        #Agrega un elemento a la pila
        self.elementos.append(elemento)
    
    def pop(self):
        #Quita y devuelve el elemento superior de la pila
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return "La pila está vacía"
    
    def peek(self):
        #Devuelve el elemento superior de la pila sin quitarlo
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return "La pila está vacía"
    
    def esta_vacia(self):
        #Devuelve True si la pila está vacía, de lo contrario False
        return len(self.elementos) == 0
    
    def __str__(self):
        #Representación en texto de la pila
        return f"Pila: {self.elementos}"