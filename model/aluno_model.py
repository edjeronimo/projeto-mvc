class Aluno:
    def _init_(self, nome, email, matricula):
        self.nome = nome
        self.email = email
        self.matricula = matricula

class CadastroAlunoModel:
    def _init_(self):
        self.alunos = []

    def adicionar_aluno(self, nome, email, matricula):
        aluno = Aluno(nome, email, matricula)
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos