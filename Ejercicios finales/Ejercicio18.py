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

    # Eliminar nodos duplicados
    def eliminar_duplicados(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        
        valores_vistos = set()
        actual = self.cabeza
        previo = None
        
        while actual:
            if actual.dato in valores_vistos:
                # Eliminar el nodo duplicado
                previo.siguiente = actual.siguiente
                print(f"Elemento duplicado {actual.dato} eliminado.")
            else:
                # Agregar valor al conjunto
                valores_vistos.add(actual.dato)
                previo = actual
            actual = actual.siguiente


lista = ListaEnlazada()

# Agregar elementos
numeros = [10, 20, 30, 20, 40, 30, 50, 60, 10]
for num in numeros:
    lista.agregar_final(num)

# Mostrar la lista original
print("\nLista original:")
lista.mostrar_lista()

# Eliminar duplicados
lista.eliminar_duplicados()

# Mostrar la lista después de eliminar duplicados
print("\nLista después de eliminar duplicados:")
lista.mostrar_lista()
