from controller.professor_controller import CadastroProfessorController
from view.professor_view import GerenciarProfessorView

if __name__ == "__main__":
    controller = CadastroProfessorController()
    view = GerenciarProfessorView(controller)
    view.iniciar()
