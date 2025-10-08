from Pessoa import Pessoa # Importação da classe Pai 

# Classe Filha, subclass, SubClasse
class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, disciplina):
        super().__init__(nome, idade, cpf, endereco, telefone)
        self.disciplina = disciplina

    # Sobrescrita de método - Polimorfismo
    def mostrar_detalhes(self):
        detalhes_pessoa =  super().mostrar_detalhes()
        return f'''{detalhes_pessoa}
    Disciplina: {self.disciplina}    

    '''