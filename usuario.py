#cria um modelo de usuário

class Usuario(object):
    #método construtor
    def __init__(self, nome, idade):
        self._nome = nome          #o _ informa que essa variável deve ser usada como se fosse private. Em python não existe variável privada, então, isso é só uma convenção para dizer que essa variável deve ser usada como se fosse private
        self._idade = idade        #o self deixa essa variável disponivel para uso dentro de todos os métodos dessa classe
    
    #inicio dos getters
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade