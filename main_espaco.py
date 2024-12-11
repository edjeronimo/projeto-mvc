from controller.espaco_controller import GerenciarEspacosController
from view.espaco_view import GerenciarEspacosView
from model.espaco_model import GerenciarEspacosModel

if __name__ == "__main__":
    model = GerenciarEspacosModel()
    controller = GerenciarEspacosController(model)
    view = GerenciarEspacosView(controller)
    view.iniciar()
