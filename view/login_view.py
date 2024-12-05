from tkinter import *

class Login(Tk):

    def __init__(self):
        super().__init__()

        self.img = PhotoImage(file="assets/imagens/cadeado.png")
        Label(self,image=self.img).pack()

#Login().mainloop()