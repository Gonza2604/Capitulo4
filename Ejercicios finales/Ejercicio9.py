class Pila:
    def __init__(self):
        self.elementos = []
    
    def push(self, elemento):
        self.elementos.append(elemento)
    
    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0


# Función para simular la calculadora
def calculadora(lista):
    pila = Pila()
    
    for item in lista:
        if isinstance(item, (int, float)):  # Si es un número
            pila.push(item)
        elif item in {'+', '-', '*', '/'}:  # Si es un operador
            if pila.esta_vacia():
                return "Error: falta un operando"
            
            b = pila.pop()  # Segundo operando
            a = pila.pop()  # Primer operando
            
            if a is None or b is None:
                return "Error: falta un operando"
            
            if item == '+':
                pila.push(a + b)
            elif item == '-':
                pila.push(a - b)
            elif item == '*':
                pila.push(a * b)
            elif item == '/':
                if b == 0:
                    return "Error: división por cero"
                pila.push(a / b)
        else:
            return "Error: entrada no válida"
    
    if pila.esta_vacia() or len(pila.elementos) > 1:
        return "Error: expresión incompleta"
    
    return pila.pop()

operaciones = [
    [3, 4, '+'],           # 3 + 4 = 7
    [5, 1, 2, '+', 4, '*', '+', 3, '-'],  # 5 + ((1 + 2) * 4) - 3 = 14
    [7, 2, '*', 3, '/'],   # (7 * 2) / 3 = 4.666...
    [5, 0, '/'],           # División por cero
    [2, '+'],              # Error: falta un operando
    [2, 3, 4, '+'],        # Error: expresión incompleta
]

for operacion in operaciones:
    resultado = calculadora(operacion)
    print(f"Entrada: {operacion} => Resultado: {resultado}")
