from model.aluno_model import AlunoModel

class AlunoController:

    def __init__(self):
        pass

    def enviar(self, infor):

        if '@' in infor:
            return AlunoModel.enviar(infor)
        return -1 #E-mail inválido!