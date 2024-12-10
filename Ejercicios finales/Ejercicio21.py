class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

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

    # Método para calcular la altura del árbol
    def calcular_altura(self):
        return self._calcular_altura_recursivo(self.raiz)

    def _calcular_altura_recursivo(self, nodo_actual):
        if not nodo_actual:
            return -1  # Altura de un árbol vacío
        altura_izquierda = self._calcular_altura_recursivo(nodo_actual.izquierdo)
        altura_derecha = self._calcular_altura_recursivo(nodo_actual.derecho)
        return 1 + max(altura_izquierda, altura_derecha)


# Pruebas
arbol = ArbolBinario()

# Insertar elementos
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arbol.insertar(elem)

# Calcular la altura del árbol
altura = arbol.calcular_altura()
print(f"La altura del árbol es: {altura}")
