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

def invertir_cadena(cadena):
    pila = Pila()
    
    for caracter in cadena:
        pila.push(caracter)
    
    # Sacar cada carácter para formar la cadena invertida
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.pop()
    
    return cadena_invertida


texto_original = "Hola mundo"
texto_invertido = invertir_cadena(texto_original)

print(f"Texto original: {texto_original}")
print(f"Texto invertido: {texto_invertido}")
