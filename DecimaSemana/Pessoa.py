# Classe Pai - Classe abstrata - SuperClass, Superclasse
class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone): # Método construtor
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
    
    def mostrar_detalhes(self):
        return f'''
    Nome: {self.nome}
    Idade: {self.idade}
    CPF: {self.cpf}
    Endereço: {self.endereco}
    Telefone: {self.telefone}    
    '''
