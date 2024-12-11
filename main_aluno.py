from controller.aluno_controler import CadastroAlunoController
from view.aluno_view import CadastroAlunoView

if __name__ == "__main__":
    controller = CadastroAlunoController()
    view = CadastroAlunoView(controller)
    view.iniciar()
