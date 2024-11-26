class BinaryTree:
    def __init__(self, value=None):
        self.value = value  # Valor del nodo
        self.left = None  # Subárbol izquierdo
        self.right = None  # Subárbol derecho
    
    def combine(self, operator, left_tree, right_tree):
        """Combina dos subárboles con un operador como raíz"""
        self.value = operator  # El valor es el operador
        self.left = left_tree  # El subárbol izquierdo
        self.right = right_tree  # El subárbol derecho
    
    def is_operand(self):
        """Devuelve True si el nodo es un operando (sin hijos)"""
        return not self.left and not self.right

def build_expression_tree(postfix_expression):
    """Construye el árbol binario a partir de la expresión postfija"""
    stack = []  # Pila para manejar los operandos y operadores
    for token in postfix_expression:
        if token.isalnum():  # Si el token es un operando
            stack.append(BinaryTree(token))  # Crear un nodo hoja
        elif token in '+-*/^':  # Si el token es un operador
            if len(stack) < 2:
                raise ValueError("Expresión postfija inválida.")  # Verifica que haya suficientes operandos
            right = stack.pop()  # Sacar el operando derecho
            left = stack.pop()  # Sacar el operando izquierdo
            new_tree = BinaryTree()  # Nuevo nodo para el operador
            new_tree.combine(token, left, right)  # Combinar los operandos con el operador
            stack.append(new_tree)  # Agregar el subárbol a la pila
        else:
            raise ValueError(f"Token desconocido: {token}")  # Token no válido
    if len(stack) != 1:
        raise ValueError("Expresión postfija inválida. Debe generar un solo árbol.")
    return stack.pop()  # El único elemento restante es el árbol

def infix_traversal(node):
    """Recorrido en infijo con paréntesis para operaciones"""
    if node is None:
        return ""
    if node.is_operand():  # Si es un operando, devolver su valor
        return node.value
    # Si no, recorrer los subárboles izquierdo y derecho con paréntesis
    return f"({infix_traversal(node.left)} {node.value} {infix_traversal(node.right)})"

def prefix_traversal(node):
    """Recorrido en preorden (prefijo)"""
    if node is None:
        return ""
    # Mostrar el valor del nodo seguido de los recorridos izquierdo y derecho
    return f"{node.value} {prefix_traversal(node.left)} {prefix_traversal(node.right)}".strip()

def postfix_traversal(node):
    """Recorrido en postorden (postfijo)"""
    if node is None:
        return ""
    # Mostrar los recorridos izquierdo y derecho seguidos del valor del nodo
    return f"{postfix_traversal(node.left)} {postfix_traversal(node.right)} {node.value}".strip()

# Ejecución de ejemplo con varias expresiones
expressions = [
    "91 95 + 15 + 19 + 4 *".split(),
    "B B * A C 4 * *".split(),
    "42".split(),
    "A 57".split(),
    "+ /".split()
]

for expr in expressions:
    try:
        print(f"Expresión: {' '.join(expr)}")
        tree = build_expression_tree(expr)  # Construir el árbol
        print("Infix:", infix_traversal(tree))  # Recorrido infijo
        print("Prefix:", prefix_traversal(tree))  # Recorrido prefijo
        print("Postfix:", postfix_traversal(tree))  # Recorrido postfijo
        print()
    except ValueError as e:
        print(f"Error: {e}")
