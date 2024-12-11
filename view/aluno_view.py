import tkinter as tk
from tkinter import messagebox

class CadastroAlunoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Cadastro de Alunos")
        self.root.geometry("400x300")

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Cadastrar Aluno", width=20, command=self.cadastrar_aluno).pack(pady=5)
        tk.Button(self.menu_frame, text="Sair", width=20, command=self.root.quit).pack(pady=5)

    def iniciar(self):
        self.root.mainloop()

    def cadastrar_aluno(self):
        def confirmar():
            nome = nome_entry.get()
            email = email_entry.get()
            matricula = matricula_entry.get()
            if nome and email and matricula:
                self.controller.adicionar_aluno(nome, email, matricula)
                messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
                janela.destroy()
            else:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Aluno")
        janela.geometry("300x200")

        tk.Label(janela, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Label(janela, text="Email:").pack(pady=5)
        email_entry = tk.Entry(janela)
        email_entry.pack(pady=5)

        tk.Label(janela, text="Matrícula:").pack(pady=5)
        matricula_entry = tk.Entry(janela)
        matricula_entry.pack(pady=5)

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)