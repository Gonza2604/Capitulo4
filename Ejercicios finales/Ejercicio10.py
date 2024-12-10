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


# Simulación del navegador
class Navegador:
    def __init__(self):
        self.historial = Pila()
        self.adelante = Pila()
    
    def visitar(self, pagina):
        print(f"Visitando: {pagina}")
        self.historial.push(pagina)
        self.adelante = Pila()  # Vaciar la pila de adelante
    
    def ir_atras(self):
        if self.historial.esta_vacia():
            print("No hay historial para ir atrás.")
            return
        
        pagina_actual = self.historial.pop()
        self.adelante.push(pagina_actual)
        
        if self.historial.esta_vacia():
            print("No hay más páginas en el historial.")
        else:
            print(f"Página actual: {self.historial.peek()}")
    
    def ir_adelante(self):
        if self.adelante.esta_vacia():
            print("No hay páginas para ir adelante.")
            return
        
        pagina = self.adelante.pop()
        self.historial.push(pagina)
        print(f"Página actual: {pagina}")


navegador = Navegador()

navegador.visitar("google.com")
navegador.visitar("facebook.com")
navegador.visitar("github.com")

# Navegar hacia atrás
navegador.ir_atras()
navegador.ir_atras()

# Ir adelante
navegador.ir_adelante()

# Visitar una nueva página
navegador.visitar("wikipedia.org")  # Vacía el historial de adelante

# Intentar ir adelante después de visitar una nueva página
navegador.ir_adelante()  # No hay páginas para ir adelante
