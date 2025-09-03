def exibir_cardapio():
    cardapio = {
    "Mussarela": 30.00,
    "Calabresa": 32.00,
    "Pepperoni": 35.00,
    "Quatro Queijos": 38.00,
    "Frango com Catupiry": 40.00
        }
    print("--- 📖 Cardápio da Pizzaria Sabores ---")
    for  preco, pizza in cardapio.items():
        print(f"🍕 {pizza}: R$ {preco:.2f}")

exibir_cardapio()