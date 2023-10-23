class Grafo:
    def __init__(self):
        # Inicializar un grafo vacío con un diccionario.
        self.grafo = {}

    def agregar_vertice(self, vertice):
        # Agregar un vértice al grafo como una clave con una lista vacía de aristas.
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        # Agregar una arista entre dos vértices al grafo.
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

def busqueda_en_profundidad(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para llevar un registro de los nodos visitados.
    camino = []  # Lista para registrar el camino actual.

    def dfs(nodo_actual):
        if nodo_actual == objetivo:
            camino.append(nodo_actual)  # Si el nodo actual es el objetivo, agregarlo al camino.
            return True

        visitados.add(nodo_actual)  # Marcar el nodo actual como visitado.
        camino.append(nodo_actual)  # Agregar el nodo actual al camino.

        for vecino in grafo.grafo[nodo_actual]:
            if vecino not in visitados and dfs(vecino):
                return True  # Si se encontró el objetivo en el vecino, terminar la búsqueda.

        camino.pop()  # Si no se encontró el objetivo, retroceder y eliminar el nodo actual del camino.
        return False

    if dfs(inicio):
        return camino  # Si se encontró un camino al objetivo, retornar el camino.
    else:
        return None  # Si no se encontró un camino al objetivo, retornar None.

# Ejemplo de uso:
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_vertice('A')
grafo_ejemplo.agregar_vertice('B')
grafo_ejemplo.agregar_vertice('C')
grafo_ejemplo.agregar_vertice('D')
grafo_ejemplo.agregar_arista('A', 'B')
grafo_ejemplo.agregar_arista('A', 'C')
grafo_ejemplo.agregar_arista('B', 'D')
grafo_ejemplo.agregar_arista('C', 'D')

inicio = 'A'
objetivo = 'D'

resultado = busqueda_en_profundidad(grafo_ejemplo, inicio, objetivo)
if resultado:
    print(f"Camino encontrado de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
