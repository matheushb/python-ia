# Matheus Hoegen Baraldi -              22158952-2
# Vitor Bussioli Jorge -                22113742-2
# José Eduardo Centenaro da Rocha -     22110027-2
# vitoria Gabriele Mendonca Mendes-     22137969-2
# Wesley dos Santos David -             22171156-2
# lucas roncon goncalves -              22014352-2
# Joao Pedro S Lussani -                22014550-2
# Anna Julia Duarte Prando -            22045748-2
# Gabriel Maiolli -                     22120200-2 
# Leonardo Franchini                    22014274-2
# João Gabriel Renzetti                 22108621-2

from collections import deque
import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_arco(self, vertice_origem, vertice_destino, peso=1):
        if vertice_origem in self.grafo:
            self.grafo[vertice_origem].append((vertice_destino, peso))
        else:
            self.grafo[vertice_origem] = [(vertice_destino, peso)]
        
        if vertice_destino in self.grafo:
            self.grafo[vertice_destino].append((vertice_origem, peso))
        else:
            self.grafo[vertice_destino] = [(vertice_origem, peso)]

    def busca_em_largura(self, vertice_inicial, target):
        print("Busca em Largura:")
        visitados = set()
        fila = deque([vertice_inicial])
        while fila:
            vertice = fila.popleft() #primeiro vertice da fila
            if vertice not in visitados:
                print(vertice)
                visitados.add(vertice)
                if vertice == target:
                    return
                for vizinho, _ in self.grafo.get(vertice, []):
                    if vizinho not in visitados:
                        fila.append(vizinho)

    def busca_em_profundidade(self, vertice_inicial, target, visitados=None):
        if visitados is None:
            print("Busca em Profundidade:")
            visitados = set()

        print(vertice_inicial)
        visitados.add(vertice_inicial)

        for vizinho, _ in self.grafo.get(vertice_inicial, []):
            if target in visitados:
                return

            if vizinho not in visitados:
                self.busca_em_profundidade(vizinho,target, visitados)

    def busca_uniforme(self, vertice_inicial, target):
        print("Busca de Custo Uniforme: ")
        fila_prioridade = [(0, vertice_inicial)]
        visitados = set()

        while fila_prioridade:
            custo_atual, vertice = heapq.heappop(fila_prioridade)

            if vertice in visitados:
                continue

            if vertice == target:
                print(f"Visitando {vertice} com custo {custo_atual}")
            visitados.add(vertice)
            for vizinho, peso in self.grafo.get(vertice, []):
                if vizinho not in visitados:
                    novo_custo = custo_atual + peso
                    heapq.heappush(fila_prioridade, (novo_custo, vizinho))
    

    def __str__(self):
        return str(self.grafo)

grafo = Grafo()

grafo.adicionar_arco('Frankfurt', 'Wuzburg', 111)
grafo.adicionar_arco('Frankfurt', 'Mannheim', 85)
grafo.adicionar_arco('Mannheim', 'Karlsruhe',67)
grafo.adicionar_arco('Mannheim', 'Numberg', 230)
grafo.adicionar_arco('Wuzburg', 'Numberg', 104)
grafo.adicionar_arco('Wuzburg', 'Ulm', 183)
grafo.adicionar_arco('Wuzburg', 'Stuttgart', 140)
grafo.adicionar_arco('Karlsruhe', 'Stuttgart', 64)
grafo.adicionar_arco('Karlsruhe', 'Basel', 191)
grafo.adicionar_arco('Basel', 'Zurich', 85)
grafo.adicionar_arco('Basel', 'Bern', 91)
grafo.adicionar_arco('Zurich', 'Bern', 120)
grafo.adicionar_arco('Zurich', 'Memmingen', 184)
grafo.adicionar_arco('Memmingen', 'Ulm', 55)
grafo.adicionar_arco('Memmingen', 'Munchen', 59)
grafo.adicionar_arco('Ulm', 'Stuttgart', 107)
grafo.adicionar_arco('Ulm', 'Munchen', 123)
grafo.adicionar_arco('Ulm', 'Numberg', 171)
grafo.adicionar_arco('Numberg', 'Bayreuth', 75)
grafo.adicionar_arco('Numberg', 'Passau', 220)
grafo.adicionar_arco('Passau', 'Linz', 102)
grafo.adicionar_arco('Linz', 'Salzburg', 126)
grafo.adicionar_arco('Salzburg', 'Rosenheim', 81)
grafo.adicionar_arco('Rosenheim', 'Innsbruck', 93)
grafo.adicionar_arco('Innsbruck', 'Landeck', 73)
grafo.adicionar_arco('Rosenheim', 'Munchen', 59)
grafo.adicionar_arco('Munchen', 'Numberg', 59)

grafo.busca_em_largura('Ulm', 'Bern')
grafo.busca_em_profundidade('Ulm', 'Bern')
grafo.busca_uniforme('Ulm', 'Bern')



