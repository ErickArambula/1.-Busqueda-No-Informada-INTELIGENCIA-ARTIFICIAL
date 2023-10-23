class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

def busqueda_bidireccional(grafo, inicio, objetivo):
    visitados_inicio = set()  # Conjunto para llevar un registro de nodos visitados desde el inicio.
    visitados_objetivo = set()  # Conjunto para llevar un registro de nodos visitados desde el objetivo.

    cola_inicio = [inicio]  # Cola para llevar un registro de nodos a explorar desde el inicio.
    cola_objetivo = [objetivo]  # Cola para llevar un registro de nodos a explorar desde el objetivo.

    camino_inicio = {}  # Diccionario para registrar el camino desde el inicio.
    camino_objetivo = {}  # Diccionario para registrar el camino desde el objetivo.

    while cola_inicio and cola_objetivo:
        # Realizar la búsqueda desde el inicio.
        nodo_actual_inicio = cola_inicio.pop(0)
        visitados_inicio.add(nodo_actual_inicio)

        # Verificar si el nodo actual desde el inicio también ha sido visitado desde el objetivo.
        if nodo_actual_inicio in visitados_objetivo:
            # Se encontró un camino desde el inicio al objetivo.
            camino_inicio[nodo_actual_inicio] = camino_objetivo[nodo_actual_inicio]
            return reconstruir_camino(inicio, objetivo, camino_inicio)

        for vecino in grafo.grafo[nodo_actual_inicio]:
            if vecino not in visitados_inicio:
                cola_inicio.append(vecino)
                camino_inicio[vecino] = nodo_actual_inicio

        # Realizar la búsqueda desde el objetivo.
        nodo_actual_objetivo = cola_objetivo.pop(0)
        visitados_objetivo.add(nodo_actual_objetivo)

        # Verificar si el nodo actual desde el objetivo también ha sido visitado desde el inicio.
        if nodo_actual_objetivo in visitados_inicio:
            # Se encontró un camino desde el inicio al objetivo.
            camino_objetivo[nodo_actual_objetivo] = camino_inicio[nodo_actual_objetivo]
            return reconstruir_camino(inicio, objetivo, camino_objetivo)

        for vecino in grafo.grafo[nodo_actual_objetivo]:
            if vecino not in visitados_objetivo:
                cola_objetivo.append(vecino)
                camino_objetivo[vecino] = nodo_actual_objetivo

    return None  # No se encontró un camino desde el inicio al objetivo.

def reconstruir_camino(inicio, objetivo, camino):
    # Reconstruir el camino desde el inicio al objetivo.
    camino_total = [objetivo]
    nodo_actual = objetivo

    while nodo_actual != inicio:
        nodo_actual = camino[nodo_actual]
        camino_total.insert(0, nodo_actual)

    return camino_total

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

resultado = busqueda_bidireccional(grafo_ejemplo, inicio, objetivo)
if resultado:
    print(f"Camino encontrado de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
