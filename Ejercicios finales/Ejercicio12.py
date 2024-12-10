class Cola:
    def __init__(self):
        self.elementos = []
    
    def enqueue(self, elemento):
        self.elementos.append(elemento)
    
    def dequeue(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0


# Simulación de atención al cliente
class Banco:
    def __init__(self):
        self.cola = Cola()
        self.numero_cliente = 0
    
    # Llega un nuevo cliente
    def llegar_cliente(self):
        self.numero_cliente += 1
        self.cola.enqueue(f"Cliente {self.numero_cliente}")
        print(f"Cliente {self.numero_cliente} ha llegado al banco.")
    
    # Atender al siguiente cliente
    def atender_cliente(self):
        if self.cola.esta_vacia():
            print("No hay clientes para atender.")
        else:
            cliente = self.cola.dequeue()
            print(f"Atendiendo a {cliente}.")
    
    # Mostrar estado actual de la cola
    def mostrar_cola(self):
        if self.cola.esta_vacia():
            print("No hay clientes en espera.")
        else:
            print("Clientes en espera:", ", ".join(self.cola.elementos))


banco = Banco()

# Llegan clientes
banco.llegar_cliente()
banco.llegar_cliente()
banco.llegar_cliente()

# Mostrar la cola
banco.mostrar_cola()

# Atender a los clientes
banco.atender_cliente()
banco.atender_cliente()

# Mostrar la cola después de atender
banco.mostrar_cola()

# Atender al último cliente
banco.atender_cliente()

# Intentar atender cuando no hay clientes
banco.atender_cliente()
