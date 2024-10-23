import tkinter as tk
from random import shuffle


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo dos 8")

        # Cria uma matriz de botões para representar as peças do jogo
        self.blocos = [[None for _ in range(3)] for _ in range(3)]
        self.empty_pos = (2, 2)  # Posição inicial do espaço vazio

        # Cria os valores das peças
        numeros = list(range(1, 9)) + [
            None
        ]  # Números de 1 a 8 + None para o espaço vazio
        shuffle(numeros)  # Embaralha os números

        self.quadro = [numeros[i : i + 3] for i in range(0, 9, 3)]  # Tabuleiro 3x3
        self.cria_quadro()

    def cria_quadro(self):
        for i in range(3):
            for j in range(3):
                num = self.quadro[i][j]
                # Cria um botão para cada peça do jogo
                if num is not None:
                    self.blocos[i][j] = tk.Button(self.root, text=str(num), font=("Arial", 24), 
                                                 width=5, height=2)
                    self.blocos[i][j].grid(row=i, column=j)
                # Cria um botão vazio para representar o espaço vazio
                else:
                    self.blocos[i][j] = tk.Button(self.root, text="", font=("Arial", 24),
                        width=5, height=2, state=tk.DISABLED)
                    self.blocos[i][j].grid(row=i, column=j)
        self.atualiza_quadro()

    def atualiza_quadro(self):
        for i in range(3):
            for j in range(3):
                num = self.quadro[i][j]
                if num is not None:
                    self.blocos[i][j].config(text=str(num), state=tk.NORMAL)
                else:
                    self.blocos[i][j].config(text="", state=tk.DISABLED)
                    
root = tk.Tk()
App(root)
root.mainloop()
