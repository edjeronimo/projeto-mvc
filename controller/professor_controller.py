class CadastroProfessorController:
    def __init__(self):
        self.professores = [
            {"nome": "João", "email": "joao@exemplo.com"},
            {"nome": "Carla", "email": "carla@exemplo.com"},
            {"nome": "Marcela", "email": "marcela@exemplo.com"},
        ]

    def listar_professores(self):
        return self.professores

    def alterar_email(self, nome, novo_email):
        for professor in self.professores:
            if professor["nome"] == nome:
                professor["email"] = novo_email
                return True
        return False
