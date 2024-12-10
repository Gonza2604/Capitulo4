class Pila:
    def __init__(self):
        self.elementos = []
    
    def push(self, elemento):
        self.elementos.append(elemento)
    
    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0


# Función para verificar el balanceo de paréntesis
def esta_balanceada(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':  # Si es un paréntesis de apertura
            pila.push(caracter)
        elif caracter in ')}]':  # Si es un paréntesis de cierre
            if pila.esta_vacia() or pila.pop() != pares[caracter]:
                return False
    
    return pila.esta_vacia()

cadenas_prueba = [
    "([])",        # Balanceada
    "{[()]}",      # Balanceada
    "([)]",        # No balanceada
    "((()))",      # Balanceada
    "({[})]",      # No balanceada
    "()",          # Balanceada
    "((}",         # No balanceada
]

for cadena in cadenas_prueba:
    resultado = "balanceada" if esta_balanceada(cadena) else "no balanceada"
    print(f"La cadena {cadena} está {resultado}.")
