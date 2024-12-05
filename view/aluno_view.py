from tkinter import *
from controller.aluno_controller import AlunoController
from tkinter import messagebox

class AlunoView(Tk):

    def __init__(self):
        super().__init__()

        self.email = Entry(self)
        self.email.pack()

        Button(self,text="Enviar",command=self.enviar).pack()

    def enviar(self):
        obj = AlunoController()
        resposta = obj.enviar(self.email.get())
        if resposta == -1:
            messagebox.showerror('Erro!','E-mail inválido!')
        elif resposta == 0:
            messagebox.showwarning('Atenção!','Houve um erro!')
        else:
            messagebox.showinfo('OK','Sucesso!')