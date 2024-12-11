class Professor:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class CadastroProfessorModel:
    def __init__(self):
        self.professores = []

    def adicionar_professor(self, nome, email):
        professor = Professor(nome, email)
        self.professores.append(professor)

    def alterar_email(self, nome, novo_email):
        for professor in self.professores:
            if professor.nome == nome:
                professor.email = novo_email
                return True
        return False