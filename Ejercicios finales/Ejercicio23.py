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

    # Método para contar nodos hoja
    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo_actual):
        if not nodo_actual:
            return 0
        
        # Si es una hoja
        if not nodo_actual.izquierdo and not nodo_actual.derecho:
            return 1
        
        # Sumar hojas de los subárboles
        hojas_izquierda = self._contar_hojas_recursivo(nodo_actual.izquierdo)
        hojas_derecha = self._contar_hojas_recursivo(nodo_actual.derecho)
        return hojas_izquierda + hojas_derecha


# Pruebas
arbol = ArbolBinario()

# Insertar elementos
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arbol.insertar(elem)

# Contar nodos hoja
hojas = arbol.contar_hojas()
print(f"El árbol tiene {hojas} nodos hoja.")
