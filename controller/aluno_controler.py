class CadastroAlunoController:
    def _init_(self, model):
        self.model = model

    def adicionar_aluno(self, nome, email, matricula):
        try:
            self.model.adicionar_aluno(nome, email, matricula)
            print(f"Aluno {nome} adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar aluno: {e}")

    
    def iniciar(self):
        self.view.iniciar()