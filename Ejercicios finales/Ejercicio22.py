from collections import deque

# Clase NodoArbol
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


# Clase ArbolBinario
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Método para insertar elementos
    def insertar(self, dato):
        if not self.raiz:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo_actual, dato):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierdo:
                self._insertar_recursivo(nodo_actual.izquierdo, dato)
            else:
                nodo_actual.izquierdo = NodoArbol(dato)
        else:
            if nodo_actual.derecho:
                self._insertar_recursivo(nodo_actual.derecho, dato)
            else:
                nodo_actual.derecho = NodoArbol(dato)

    # Método para recorrido por niveles
    def recorrido_por_niveles(self):
        if not self.raiz:
            print("El árbol está vacío.")
            return
        
        cola = deque([self.raiz])  # Inicializamos la cola con la raíz
        print("Recorrido por niveles:", end=" ")

        while cola:
            nodo_actual = cola.popleft()  # Extraemos el primer nodo
            print(nodo_actual.dato, end=" ")

            # Agregamos los hijos del nodo actual
            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)
            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)
        print()


# Pruebas
arbol = ArbolBinario()

# Insertar elementos
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arbol.insertar(elem)

# Recorrido por niveles
arbol.recorrido_por_niveles()
