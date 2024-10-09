from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}
        self.vertices = []

    def adicionar_aresta(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
            self.vertices.append(u)
        if v not in self.grafo:
            self.grafo[v] = []
            self.vertices.append(v)
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def bfs(self, inicio, objetivo):
        visitado = {vertice: False for vertice in self.grafo}
        antecessor = {vertice: None for vertice in self.grafo}
        fila = deque([inicio])
        visitado[inicio] = True

        while fila:
            vertice_atual = fila.popleft()
            if vertice_atual == objetivo:
                return self.reconstruir_caminho(antecessor, inicio, objetivo)

            for vizinho in self.grafo[vertice_atual]:
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

    def desenhar_grafo_ascii(self):
        print("\nGrafo em formato ascii:")
        
        for vertice in self.grafo:
            conexoes = ' - '.join(self.grafo[vertice])
            print(f"{vertice}: {conexoes}")

def interface_usuario():
    grafo = Grafo()

    while True:
        print("\nEscolha uma ação:")
        print("1. Adicionar uma aresta")
        print("2. Executar busca em largura (BFS)")
        print("3. Exibir o grafo")
        print("4. Desenhar o grafo em ascii")
        print("5. Sair")

        escolha = input("Digite o numero da ação desejada: ")

        if escolha == '1':
            u = input("Digite o vértice de origem: ")
            v = input("Digite o vértice de destino: ")
            grafo.adicionar_aresta(u, v)
            print(f"Aresta adicionada entre {u} e {v}.")
        elif escolha == '2':
            inicio = input("Digite o vértice de início: ")
            objetivo = input("Digite o vértice de objetivo: ")
            caminho = grafo.bfs(inicio, objetivo)
            if caminho:
                print(f"Caminho mais curto entre {inicio} e {objetivo}: {' -> '.join(caminho)}")
            else:
                print(f"Não existe caminho entre {inicio} e {objetivo}")
        elif escolha == '3':
            print("Grafo atual:", dict(grafo.grafo))
        elif escolha == '4':
            grafo.desenhar_grafo_ascii()
        elif escolha == '5':
            print("Encerrando o programa")
            break
        else:
            print("opção inválida")

interface_usuario()
