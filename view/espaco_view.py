import tkinter as tk
from tkinter import messagebox

class GerenciarEspacosView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Gerenciar Espaços")
        self.root.geometry("400x300")

        tk.Button(self.root, text="Listar Espaços", width=20, command=self.listar_espacos).pack(pady=5)
        tk.Button(self.root, text="Excluir Espaço", width=20, command=self.excluir_espaco).pack(pady=5)
        tk.Button(self.root, text="Sair", width=20, command=self.root.quit).pack(pady=5)

    def iniciar(self):
        self.root.mainloop()

    def listar_espacos(self):
        espacos = self.controller.listar_espacos()
        lista = "\n".join(espacos)
        messagebox.showinfo("Espaços Disponíveis", lista)

    def excluir_espaco(self):
        def confirmar():
            nome = nome_entry.get()
            if self.controller.excluir_espaco(nome):
                messagebox.showinfo("Sucesso", f"Espaço {nome} excluído com sucesso!")
                janela.destroy()
            else:
                messagebox.showerror("Erro", f"Espaço {nome} não encontrado.")

        janela = tk.Toplevel(self.root)
        janela.title("Excluir Espaço")
        janela.geometry("300x150")

        tk.Label(janela, text="Nome do Espaço:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
