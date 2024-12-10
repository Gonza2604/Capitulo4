class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Agregar un elemento al final
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Elemento {dato} agregado al final.")

    # Eliminar un elemento específico
    def eliminar(self, dato):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Elemento {dato} eliminado.")
            return
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        
        if not actual.siguiente:
            print(f"Elemento {dato} no encontrado.")
        else:
            actual.siguiente = actual.siguiente.siguiente
            print(f"Elemento {dato} eliminado.")

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                print(f"Elemento {dato} encontrado en la posición {posicion}.")
                return posicion
            actual = actual.siguiente
            posicion += 1
        print(f"Elemento {dato} no encontrado.")
        return -1

    # Mostrar la lista
    def mostrar_lista(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Lista:", elementos)

    # Método para invertir la lista
    def invertir(self):
        previo = None
        actual = self.cabeza
        
        while actual:
            siguiente = actual.siguiente  # Guardar el siguiente nodo
            actual.siguiente = previo    # Invertir el enlace
            previo = actual              # Avanzar 'previo' al nodo actual
            actual = siguiente           # Avanzar 'actual' al siguiente nodo
        
        self.cabeza = previo
        print("Lista invertida.")


lista = ListaEnlazada()

# Agregar elementos
lista.agregar_final(10)
lista.agregar_final(20)
lista.agregar_final(30)
lista.agregar_final(40)

# Mostrar la lista original
print("Lista original:")
lista.mostrar_lista()

# Invertir la lista
lista.invertir()

# Mostrar la lista invertida
print("Lista después de invertir:")
lista.mostrar_lista()
