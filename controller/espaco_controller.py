class GerenciarEspacosController:
    def __init__(self, model):
        self.model = model

    def listar_espacos(self):
        return self.model.listar_espacos()

    def excluir_espaco(self, nome):
        if self.model.excluir_espaco(nome):
            return f"Espaço {nome} excluído com sucesso!"
        else:
            return f"Erro: Espaço {nome} não encontrado."
