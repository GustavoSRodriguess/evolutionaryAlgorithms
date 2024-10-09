import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

#necessário instalar as bibliotecas networkx e matplotlib
class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def adicionar_aresta(self, u, v):
        self.grafo.add_edge(u, v)
        print(f"Aresta adicionada entre {u} e {v}.")

    def bfs(self, inicio, objetivo):
        visitado = {vertice: False for vertice in self.grafo.nodes()}
        antecessor = {vertice: None for vertice in self.grafo.nodes()}
        fila = deque([inicio])
        visitado[inicio] = True

        while fila:
            vertice_atual = fila.popleft()
            if vertice_atual == objetivo:
                return self.reconstruir_caminho(antecessor, inicio, objetivo)

            for vizinho in self.grafo.neighbors(vertice_atual):
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    antecessor[vizinho] = vertice_atual
                    fila.append(vizinho)

        return None

    def reconstruir_caminho(self, antecessor, inicio, objetivo):
        caminho = []
        vertice_atual = objetivo
        while vertice_atual is not None:
            caminho.append(vertice_atual)
            vertice_atual = antecessor[vertice_atual]
        caminho.reverse()
        return caminho

    def desenhar_grafo(self):
        pos = nx.spring_layout(self.grafo) 
        nx.draw(self.grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.show()

def interface_usuario():
    grafo = Grafo()

    while True:
        print("\nEscolha uma ação:")
        print("1. Adicionar uma aresta")
        print("2. Executar Busca em Largura (BFS)")
        print("3. Exibir o grafo")
        print("4. Desenhar o grafo")
        print("5. Sair")

        escolha = input("Digite o numero da ação desejada: ")

        if escolha == '1':
            u = input("Digite o vértice de origem: ")
            v = input("Digite o vértice de destino: ")
            grafo.adicionar_aresta(u, v)
        elif escolha == '2':
            inicio = input("Digite o vértice de início: ")
            objetivo = input("Digite o vértice de objetivo: ")
            caminho = grafo.bfs(inicio, objetivo)
            if caminho:
                print(f"caminho mais curto de {inicio} a {objetivo}: {' -> '.join(caminho)}")
            else:
                print(f"não existe caminho entre {inicio} e {objetivo}")
        elif escolha == '3':
            print("Grafo atual:", dict(grafo.grafo.adjacency()))
        elif escolha == '4':
            grafo.desenhar_grafo() 
        elif escolha == '5':
            print("Encerrando o programa")
            break
        else:
            print("Escolha invalida")

interface_usuario()
