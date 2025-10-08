from Professor import Professor
from Aluno import Aluno
from Funcionario import Funcionario

def main():

    aluno1 = Aluno("João Silva", 20, "123.456.789-10","Rua A, 123", "91234-5678", "2023001")
    professor1 = Professor("Maria Oliveira", 35, "987.654.321-00", "Rua B, 456", "998765698", "Matemática")
    funcionario1 = Funcionario("Carlos Souza", 40, "111.222.333-44", "Rua C, 789", "98654565", "Secretário")

    print('      Detalhes do Aluno: ')
    print(aluno1.mostrar_detalhes())
    print('\n ---------------------------')
    print('\n    Detalhes do Professor: ')
    print(professor1.mostrar_detalhes())
    print('\n ---------------------------')
    print('\n    Detalhes do Funcionário: ')
    print(funcionario1.mostrar_detalhes())

if __name__ == '__main__':
    main()

