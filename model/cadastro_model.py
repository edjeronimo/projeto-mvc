
class CadrastroModel:
    __nome : str
    __email = str
    __senha = str
    __token = "e33e2e12e2"
    
    def __init__(self,nome='',email='',senha=''):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        
    def _toMap(self):
        return {
            'nome': self.__nome,
            'email': self.__email,
            'senha': self.__senha
        }
        
    def fromMap(self, map={}):
        return {
            'nome': map['nome']
        }
    
        
    def __getToken(self):
        return self.__token
    
    def getNome(self):
        verificacao = self.__getToken()
        if(verificacao == 'e33e2e12e2'):
            return self.__nome
        return False
    
CadrastroModel()