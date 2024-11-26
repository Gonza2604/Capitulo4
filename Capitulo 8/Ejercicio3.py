import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char  # Carácter
        self.freq = freq  # Frecuencia
        self.left = None   # Subárbol izquierdo
        self.right = None  # Subárbol derecho

    # Comparar nodos para que puedan ser usados en una heap (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.codes = {}  # Diccionario de códigos Huffman
        self.reverse_codes = {}  # Diccionario inverso para la decodificación
        self.tree_root = None  # Raíz del árbol de Huffman
    
    def build_tree(self, text):
        """Construye el árbol de Huffman a partir del texto"""
        # Contar la frecuencia de cada carácter en el texto
        freq = defaultdict(int)
        for char in text:
            freq[char] += 1
        
        # Crear nodos para cada carácter
        priority_queue = [Node(char, f) for char, f in freq.items()]
        heapq.heapify(priority_queue)
        
        # Construir el árbol de Huffman
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)
        
        # La raíz del árbol de Huffman
        self.tree_root = priority_queue[0]
        
        # Generar los códigos Huffman
        self._generate_codes(self.tree_root, "")

    def _generate_codes(self, node, current_code):
        """Genera los códigos Huffman recursivamente"""
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self, text):
        """Codifica el texto usando los códigos Huffman"""
        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text

    def decode(self, encoded_text):
        """Decodifica el texto binario usando los códigos Huffman"""
        decoded_text = ""
        current_code = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded_text += self.reverse_codes[current_code]
                current_code = ""
        return decoded_text
    
    def print_tree(self):
        """Imprime el árbol de Huffman (para mensajes breves)"""
        self._print_tree(self.tree_root, "")
    
    def _print_tree(self, node, indent):
        """Imprime el árbol de Huffman de manera legible"""
        if node is not None:
            if node.char:
                print(f"{indent}{node.char}: {node.freq}")
            else:
                print(f"{indent}* {node.freq}")
            self._print_tree(node.left, indent + "  ")
            self._print_tree(node.right, indent + "  ")

# Función principal
def main():
    message = input("Introduce un mensaje de texto: ")
    
    huffman_coding = HuffmanCoding()
    
    # Paso 1: Construir el árbol de Huffman
    huffman_coding.build_tree(message)
    
    # Paso 2: Codificar el mensaje
    encoded_message = huffman_coding.encode(message)
    
    # Paso 3: Decodificar el mensaje
    decoded_message = huffman_coding.decode(encoded_message)
    
    # Paso 4: Mostrar la información
    print("\nTabla de códigos Huffman:")
    for char, code in huffman_coding.codes.items():
        print(f"'{char}': {code}")
    
    print("\nMensaje original:", message)
    print("Mensaje codificado:", encoded_message)
    print("Mensaje decodificado:", decoded_message)
    
    # Mostrar estadísticas
    print(f"\nLongitud del mensaje original: {len(message)} caracteres")
    print(f"Longitud del mensaje codificado: {len(encoded_message)} bits")
    
    # Mostrar el árbol de Huffman si el mensaje es breve
    if len(message) <= 20:
        print("\nÁrbol de Huffman:")
        huffman_coding.print_tree()

# Ejecutar el programa
if __name__ == "__main__":
    main()
