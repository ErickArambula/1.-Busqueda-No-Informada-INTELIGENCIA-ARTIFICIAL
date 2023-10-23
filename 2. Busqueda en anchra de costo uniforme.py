import heapq

class GrafoPonderado:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2, costo):
        self.grafo[vertice1].append((vertice2, costo))
        self.grafo[vertice2].append((vertice1, costo))

def busqueda_en_anchura_costo_uniforme(grafo, inicio, objetivo):
    visitados = set()
    cola = [(0, inicio)]  # Cola de prioridad para mantener el costo acumulado.
    camino = {}

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual == objetivo:
            # Reconstruir el camino desde el objetivo hasta el inicio.
            camino_recuperado = []
            while nodo_actual is not None:
                camino_recuperado.insert(0, nodo_actual)
                nodo_actual = camino.get(nodo_actual, None)
            return camino_recuperado

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo_arista in grafo.grafo[nodo_actual]:
                if vecino not in visitados:
                    costo_total = costo_actual + costo_arista
                    heapq.heappush(cola, (costo_total, vecino))
                    camino[vecino] = nodo_actual

    return None  # No se encontró un camino al objetivo

# Ejemplo de uso:
grafo_ponderado_ejemplo = GrafoPonderado()
grafo_ponderado_ejemplo.agregar_vertice('A')
grafo_ponderado_ejemplo.agregar_vertice('B')
grafo_ponderado_ejemplo.agregar_vertice('C')
grafo_ponderado_ejemplo.agregar_vertice('D')
grafo_ponderado_ejemplo.agregar_arista('A', 'B', 3)
grafo_ponderado_ejemplo.agregar_arista('A', 'C', 1)
grafo_ponderado_ejemplo.agregar_arista('B', 'D', 5)
grafo_ponderado_ejemplo.agregar_arista('C', 'D', 2)

inicio = 'A'
objetivo = 'D'

resultado = busqueda_en_anchura_costo_uniforme(grafo_ponderado_ejemplo, inicio, objetivo)
if resultado:
    print(f"Camino más corto de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
