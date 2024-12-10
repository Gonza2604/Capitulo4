class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Método para insertar un elemento
    def insertar(self, dato):
        if not self.raiz:
            self.raiz = NodoArbol(dato)
            print(f"Elemento {dato} insertado como raíz.")
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo_actual, dato):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierdo:
                self._insertar_recursivo(nodo_actual.izquierdo, dato)
            else:
                nodo_actual.izquierdo = NodoArbol(dato)
                print(f"Elemento {dato} insertado a la izquierda de {nodo_actual.dato}.")
        elif dato > nodo_actual.dato:
            if nodo_actual.derecho:
                self._insertar_recursivo(nodo_actual.derecho, dato)
            else:
                nodo_actual.derecho = NodoArbol(dato)
                print(f"Elemento {dato} insertado a la derecha de {nodo_actual.dato}.")
        else:
            print(f"Elemento {dato} ya existe en el árbol.")

    # Recorrido en orden (inorder)
    def recorrido_inorder(self):
        print("Recorrido en orden:")
        self._recorrido_inorder_recursivo(self.raiz)
        print()

    def _recorrido_inorder_recursivo(self, nodo_actual):
        if nodo_actual:
            self._recorrido_inorder_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.dato, end=" ")
            self._recorrido_inorder_recursivo(nodo_actual.derecho)

    # Método para buscar un elemento
    def buscar(self, dato):
        encontrado = self._buscar_recursivo(self.raiz, dato)
        if encontrado:
            print(f"Elemento {dato} encontrado en el árbol.")
        else:
            print(f"Elemento {dato} no encontrado en el árbol.")
        return encontrado

    def _buscar_recursivo(self, nodo_actual, dato):
        if not nodo_actual:
            return False
        if dato == nodo_actual.dato:
            return True
        elif dato < nodo_actual.dato:
            return self._buscar_recursivo(nodo_actual.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, dato)


arbol = ArbolBinario()

# Insertar elementos
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arbol.insertar(elem)

# Recorrido en orden
arbol.recorrido_inorder()

# Búsqueda de elementos
arbol.buscar(40)
arbol.buscar(90)
