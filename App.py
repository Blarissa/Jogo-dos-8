import tkinter as tk
import BFS
from random import shuffle

FONTE = ("Arial", 24)
COR = "#4682B4"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo dos 8")

        # Cria uma matriz de botões para representar as peças do jogo e o espaço vazio
        self.blocos = [[None for _ in range(3)] for _ in range(4)]

        # Cria os valores das peças
        numeros = list(range(1, 9)) + [None]
        shuffle(numeros)  # Embaralha os números

        self.quadro = [numeros[i : i + 3] for i in range(0, 9, 3)]

        self.empty_pos = self.retorna_empty_pos()

        self.cria_quadro()

        # Quando um botão é clicado, move a peça para o espaço vazio
        self.evento()

    def retorna_empty_pos(self):
        for i in range(3):
            for j in range(3):
                if self.quadro[i][j] == None:
                    return i, j

    # Reinicia o jogo
    def reiniciar(self):
        numeros = list(range(1, 9)) + [None]
        shuffle(numeros)
        self.quadro = [numeros[i : i + 3] for i in range(0, 9, 3)]
        self.empty_pos = (2, 2)
        self.atualiza_quadro()

    # Resolve o jogo
    def resolver(self):
        bfs = BFS.bfs(self.quadro)
        solucao = bfs.caminho
        bfs.retorna_passos(solucao)

    # Atualiza o quadro do jogo
    def atualiza_quadro(self):
        for i in range(3):
            for j in range(3):
                num = self.quadro[i][j]
                self.blocos[i][j].config(text=str(num) if num is not None else "")

    # Adiciona o evento de clique para cada botão
    def evento(self):
        for i in range(3):
            for j in range(3):
                self.blocos[i][j].config(command=lambda i=i, j=j: self.move(i, j))

    # Move a peça para o espaço vazio
    def move(self, i, j):
        x, y = self.empty_pos
        # Verifica se a peça clicada é adjacente ao espaço vazio
        if (i == x and abs(j - y) == 1) or (j == y and abs(i - x) == 1):
            self.quadro[x][y], self.quadro[i][j] = self.quadro[i][j], self.quadro[x][y]
            self.empty_pos = (i, j)
            self.atualiza_quadro()

    # Cria o quadro do jogo
    def cria_quadro(self):
        for i in range(3):
            for j in range(3):
                num = self.quadro[i][j]
                # Cria um botão para cada peça do jogo
                if num is not None:
                    self.botao_num(i, j, num)

                # Cria um botão vazio para representar o espaço vazio
                else:
                    self.botao_num(i, j, None)

        # Criar botões para reiniciar, sair e resolver o jogo
        self.botao_reiniciar()
        self.botao_sair()
        self.botao_resolver()

        self.atualiza_quadro()

    def botao_num(self, i, j, num):
        texto = "" if num is None else str(num)
        
        self.blocos[i][j] = tk.Button(
                    self.root,
                    text=texto,
                    bg=COR,
                    fg="white",
                    font=FONTE,
                    width=8,
                    height=2,
                )
        self.blocos[i][j].grid(row=i, column=j)

    def botao_resolver(self):
        self.blocos[3][2] = tk.Button(
            self.root,
            text="Resolver",
            bg=COR,
            fg="white",
            font=FONTE,
            width=8,
            height=2,
            command=self.resolver,
        )

        self.blocos[3][2].grid(row=3, column=2)

    def botao_sair(self):
        self.blocos[3][1] = tk.Button(
            self.root,
            text="Sair",
            bg=COR,
            fg="white",
            font=FONTE,
            width=8,
            height=2,
            command=self.root.quit,
        )

        self.blocos[3][1].grid(row=3, column=1)

    def botao_reiniciar(self):
        self.blocos[3][0] = tk.Button(
            self.root,
            text="Reiniciar",
            bg=COR,
            fg="white",
            font=FONTE,
            width=8,
            height=2,
            command=self.reiniciar,
        )

        self.blocos[3][0].grid(row=3, column=0)
