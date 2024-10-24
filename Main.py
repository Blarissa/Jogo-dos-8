import tkinter as tk
import BFS, App

root = tk.Tk()
app = App.App(root)

grafo = [[2, 3, 5], [4, 1, 8], [7, 6, None]]

solucao = BFS.bfs(grafo).caminho


def retorna_passos(solucao):
    if solucao:
        print(f"Solução encontrada em {len(solucao)} passos!")
        for passo in solucao:
            for linha in passo:
                print(linha)
            print("----")


retorna_passos(solucao)
root.mainloop()