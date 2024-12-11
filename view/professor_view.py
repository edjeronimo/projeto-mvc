import tkinter as tk
from tkinter import messagebox

class GerenciarProfessorView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Gerenciar Professores")
        self.root.geometry("400x300")

        self.professores = [
            {"nome": "João", "email": "joao@exemplo.com"},
            {"nome": "Carla", "email": "carla@exemplo.com"},
            {"nome": "Marcela", "email": "marcela@exemplo.com"},
        ]

        tk.Button(self.root, text="Listar Professores", width=20, command=self.listar_professores).pack(pady=5)
        tk.Button(self.root, text="Alterar Email", width=20, command=self.alterar_email).pack(pady=5)
        tk.Button(self.root, text="Sair", width=20, command=self.root.quit).pack(pady=5)

    def iniciar(self):
        self.root.mainloop()

    def listar_professores(self):
        lista = "\n".join([f"{p['nome']} - {p['email']}" for p in self.professores])
        messagebox.showinfo("Professores", lista)

    def alterar_email(self):
        def confirmar():
            nome = nome_entry.get()
            novo_email = email_entry.get()
            for professor in self.professores:
                if professor["nome"] == nome:
                    professor["email"] = novo_email
                    messagebox.showinfo("Sucesso", f"Email alterado para {novo_email}.")
                    janela.destroy()
                    return
            messagebox.showerror("Erro", "Professor não encontrado!")

        janela = tk.Toplevel(self.root)
        janela.title("Alterar Email")
        janela.geometry("300x150")

        tk.Label(janela, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Label(janela, text="Novo Email:").pack(pady=5)
        email_entry = tk.Entry(janela)
        email_entry.pack(pady=5)

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
