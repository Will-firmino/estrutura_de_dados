class Carro:
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        
    def abastecer(self):
        self.qtd_combustivel += 20
        
    # Se o carro já está ligado -> exibir mensagem que o carro já estava ligado
    # Se o carro está desligado -> liga ele
    def ligar(self):
        if self.is_ligado: # verificando se o is_ligado é True
            print("🚗 O carro já estava ligado!")
        else:
            self.is_ligado = True
            print("🚘 O carro foi ligado.")
            
            
    def desligar(self):
        if self.is_ligado == False:
            print("🚗 O carro já estava desligado!")
        else: 
          self.is_ligado = False
          print("🚘 O carro foi desligado.")

            
            
            
   # def ligar(self): # quero ligar o carro, a exceção é se ele estiver ligado.
    #     if self.is_ligado:
    #         print("🚗 O carro já estava ligado!")
    #         return
    #     self.is_ligado = True 
    #     print("🚘 O carro foi ligado.")
