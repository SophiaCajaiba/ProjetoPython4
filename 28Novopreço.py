# Calcule o novo preço de acordo com as condições.


def calcular_preco(preco, venda_mensal):
    # Processamento
    novo_preco = preco

    if venda_mensal < 500 and preco < 30:
        novo_preco = preco * 1.10

    elif venda_mensal >= 500 and venda_mensal < 1000 and preco >= 30 and preco < 80:
        novo_preco = preco * 1.15

    elif venda_mensal >= 1000 and preco >= 80:
        novo_preco = preco * 0.95

    # Mostrar resultado
    print("Preço novo:", novo_preco)


def main():
    # Entrada de dados
    preco = float(input("Digite o preço atual: "))
    venda_mensal = int(input("Digite a venda mensal: "))

    calcular_preco(preco, venda_mensal)


main()