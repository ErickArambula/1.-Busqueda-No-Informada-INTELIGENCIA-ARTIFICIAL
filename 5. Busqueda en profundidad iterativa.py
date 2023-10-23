class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)

def busqueda_en_profundidad_iterativa(grafo, inicio, objetivo, profundidad_maxima):
    for profundidad in range(profundidad_maxima + 1):
        visitados = set()  # Conjunto para llevar un registro de los nodos visitados.
        camino = []  # Lista para registrar el camino actual.

        def dls(nodo_actual):
            if nodo_actual == objetivo:
                camino.append(nodo_actual)  # Si el nodo actual es el objetivo, agregarlo al camino.
                return True

            visitados.add(nodo_actual)  # Marcar el nodo actual como visitado.
            camino.append(nodo_actual)  # Agregar el nodo actual al camino.

            if profundidad == 0:
                return False  # No explorar más allá de la profundidad máxima actual.

            for vecino in grafo.grafo[nodo_actual]:
                if vecino not in visitados and dls(vecino):
                    return True  # Si se encontró el objetivo en el vecino, terminar la búsqueda.

            camino.pop()  # Si no se encontró el objetivo, retroceder y eliminar el nodo actual del camino.
            return False

        if dls(inicio):
            return camino  # Si se encontró un camino al objetivo, retornar el camino.

    return None  # Si no se encontró un camino al objetivo dentro de la profundidad máxima.

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
profundidad_maxima = 3  # Establecer la profundidad máxima.

resultado = busqueda_en_profundidad_iterativa(grafo_ejemplo, inicio, objetivo, profundidad_maxima)
if resultado:
    print(f"Camino encontrado de {inicio} a {objetivo} (profundidad máxima {profundidad_maxima}): {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo} dentro de la profundidad máxima.")
