from collections import deque

class bfs:
    def __init__(self, grafo):
        self.grafo = grafo

        # Movimentos possíveis: (linha, coluna)
        self.movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Solução do problema
        self.solucao = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

        self.caminho = self.bfs()

    # Encontra a posição do espaço vazio
    def encontra_vazio(self, estado):
        for i in range(3):
            for j in range(3):
                if estado[i][j] is None:
                    return i, j

    # Gera os vizinhos de um estado
    def gera_vizinhos(self, estado):
        i, j = self.encontra_vazio(estado)
        vizinhos = []

        for movimento in self.movimentos:
            x, y = i + movimento[0], j + movimento[1]

            # Verifica se o movimento é válido
            if 0 <= x < 3 and 0 <= y < 3:
                # Cria um novo estado trocando o espaço vazio com a peça adjacente
                vizinho = [linha[:] for linha in estado]
                # Troca o espaço vazio com a peça adjacente
                vizinho[i][j], vizinho[x][y] = vizinho[x][y], vizinho[i][j]
                vizinhos.append(vizinho)

        return vizinhos

    # função de busca em largura
    def bfs(self):
        # Conjunto de estados visitados e fila de estados a visitar
        visitados = set()
        fila = deque([(self.grafo, [])])

        # Enquanto a fila não estiver vazia
        while fila:
            # Remove o primeiro elemento da fila e desempacota o estado e a profundidade
            estado, caminho = fila.popleft()
            visitados.add(str(estado))

            # Se o estado atual é a solução, retorna o caminho
            if estado == self.solucao:
                return caminho

            # Gerar vizinhos do estado atual e adicionar na fila
            for vizinho in self.gera_vizinhos(estado):
                if str(vizinho) not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

        return

    def retorna_passos(self, caminho):
        for i in range(len(caminho)):
            print(f"Passo {i + 1}:")
            for linha in caminho[i]:
                print(linha)
            print('{:-<13}'.format(''))
    