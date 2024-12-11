class GerenciarEspacosModel:
    def __init__(self):
        self.espacos = ["Auditório", "Informática", "Biblioteca"]

    def listar_espacos(self):
        return self.espacos

    def excluir_espaco(self, nome):
        if nome in self.espacos:
            self.espacos.remove(nome)
            return True
        return False
