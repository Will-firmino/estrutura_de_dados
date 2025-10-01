# Classe filha - subclass()
from PizzaPadrao import PizzaPadrao
class PizzaDoce(PizzaPadrao):
    def __init__(self, sabor, tamanho, preco, ingredientes, borda_recheada):
        super().__init__(sabor, tamanho, preco, ingredientes)
        self.borda_recheada = borda_recheada
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
        Borda recheada: {self.borda_recheada}
        ''')


