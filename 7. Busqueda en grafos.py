class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        # Agregar un vértice al grafo como una clave con una lista vacía de aristas.
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        # Agregar una arista entre dos vértices al grafo.
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

def busqueda_en_grafos(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para llevar un registro de nodos visitados.
    cola = [inicio]  # Cola para llevar un registro de nodos a explorar.

    while cola:
        nodo_actual = cola.pop(0)  # Tomar el primer nodo de la cola.

        if nodo_actual == objetivo:
            return True  # Se encontró el objetivo.

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcar el nodo actual como visitado.

            for vecino in grafo.grafo[nodo_actual]:
                if vecino not in visitados:
                    cola.append(vecino)  # Agregar vecinos no visitados a la cola.

    return False  # No se encontró el objetivo en el grafo.

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

resultado = busqueda_en_grafos(grafo_ejemplo, inicio, objetivo)
if resultado:
    print(f"Se encontró un camino de {inicio} a {objetivo} en el grafo.")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo} en el grafo.")
