from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}   # Inicializar un grafo vacío con un diccionario.

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:     # Agregar un vértice al grafo como una clave con una lista vacía de aristas.
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        # Agregar una arista bidireccional entre dos vértices al grafo.
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

def busqueda_en_anchura(grafo, inicio, objetivo):
    # Inicializar un conjunto para llevar un registro de nodos visitados.
    visitados = set()
    
    # Inicializar una cola para llevar un registro de nodos a explorar.
    cola = deque()
    
    # Inicializar un diccionario para seguir el camino desde el inicio hasta cada nodo visitado.
    camino = {}

    # Agregar el nodo de inicio a la cola y marcarlo como visitado.
    cola.append(inicio)
    visitados.add(inicio)

    # Comenzar la búsqueda en anchura.
    while cola:
        # Tomar el nodo actual de la cola.
        nodo_actual = cola.popleft()
        
        # Verificar si es el nodo objetivo.
        if nodo_actual == objetivo:
            # Reconstruir el camino desde el objetivo hasta el inicio.
            camino_recuperado = []
            while nodo_actual is not None:
                camino_recuperado.insert(0, nodo_actual)
                nodo_actual = camino.get(nodo_actual, None)
            return camino_recuperado

        # Explorar los vecinos del nodo actual.
        for vecino in grafo.grafo[nodo_actual]:
            if vecino not in visitados:
                # Agregar el vecino a la cola y marcarlo como visitado.
                cola.append(vecino)
                visitados.add(vecino)
                # Registrar el camino desde el nodo actual hasta el vecino.
                camino[vecino] = nodo_actual

    # Si no se encontró un camino al objetivo, retornar None.
    return None

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

resultado = busqueda_en_anchura(grafo_ejemplo, inicio, objetivo)
if resultado:
    print(f"Camino encontrado de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
