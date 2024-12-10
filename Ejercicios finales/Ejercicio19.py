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


# Función para combinar dos listas enlazadas ordenadas
def combinar_listas_ordenadas(lista1, lista2):
    nueva_lista = ListaEnlazada()

    actual1 = lista1.cabeza
    actual2 = lista2.cabeza

    while actual1 and actual2:
        if actual1.dato <= actual2.dato:
            nueva_lista.agregar_final(actual1.dato)
            actual1 = actual1.siguiente
        else:
            nueva_lista.agregar_final(actual2.dato)
            actual2 = actual2.siguiente

    # Agregar nodos restantes de ambas listas
    while actual1:
        nueva_lista.agregar_final(actual1.dato)
        actual1 = actual1.siguiente

    while actual2:
        nueva_lista.agregar_final(actual2.dato)
        actual2 = actual2.siguiente

    return nueva_lista


# Pruebas
lista1 = ListaEnlazada()
lista2 = ListaEnlazada()

# Agregar elementos a la primera lista
for num in [1, 3, 5, 7, 9]:
    lista1.agregar_final(num)

# Agregar elementos a la segunda lista
for num in [2, 4, 6, 8, 10]:
    lista2.agregar_final(num)

# Mostrar las listas originales
print("Lista 1:")
lista1.mostrar_lista()

print("Lista 2:")
lista2.mostrar_lista()

# Combinar ambas listas
lista_combinada = combinar_listas_ordenadas(lista1, lista2)

# Mostrar la lista combinada
print("\nLista combinada:")
lista_combinada.mostrar_lista()
