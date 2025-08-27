# 1. Crie um programa que aceite pedidos de um e-commerce até que o cliente digite sair.
print("Faça o seu pedido ou digite 'sair' para encerrar") 
pedido = "" #String porque 'sair' é um texto.
lista = ["Smartphone", "SmartTV", "Geladeira", "Videogame", "Fogão", "Relógio", "Notebook"]

while pedido.lower() != "sair": 
    pedido = input("Digite um produto da lista:")
    if pedido in lista:
        print(f"➡️ {pedido} adicionado ao seu carrinho!")
    elif pedido.lower() == "sair":
        print("🛒Pedido encerrado")
    else:
        print("Esse produto não está na lista. Escolha outro: ")

