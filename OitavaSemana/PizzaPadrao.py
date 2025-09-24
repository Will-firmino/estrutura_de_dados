# Classe pai - superclass()
class PizzaPadrao:
    def __init__(self, sabor, tamanho, preco, ingredientes):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingredientes = ingredientes

    def mostrar_detalhes(self):
        print(f'''
        ---🍕 Detalhes da Pizza ---
                Sabor: {self.sabor}
                Tamanho: {self.tamanho}
                Preço: {self.preco}
                Ingredientes: {self.ingredientes}
            ''')
        
pizza_calabresa = PizzaPadrao("Calabresa", "Pequeno", 50.00, "Tomate, oregano")
pizza_marguerita = PizzaPadrao("Marguerita", "Médio", 55.00, "Tomate, oregano, queijo")

# pizza_calabresa.mostrar_detalhes()
# pizza_marguerita.mostrar_detalhes()

