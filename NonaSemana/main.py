from PizzaPadrao import PizzaPadrao
from PizzaDoce import PizzaDoce

def main():
    pizza_calabresa = PizzaPadrao("Calabresa", "Pequeno", 50.00, "Tomate, oregano")
    pizza_marguerita = PizzaPadrao("Marguerita", "Médio", 55.00, "Tomate, oregano, queijo")
    pizza_comum = PizzaPadrao("Calabresa", "Família", 29.90, "Tomate, cebola")
    pizza_chocolate = PizzaDoce("Chocolate com Morango", "Pequena", 31.90, "Chocolate, Morango", "chocolate")

    pizza_calabresa.mostrar_detalhes()
    pizza_marguerita.mostrar_detalhes()

    print(" --- Pizza Comum --- ")
    pizza_comum.mostrar_detalhes()
    print(" --- Pizza Doce --- ")
    pizza_chocolate.mostrar_detalhes()

if __name__ == "__main__":
    main()