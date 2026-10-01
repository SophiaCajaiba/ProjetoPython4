# Exercício 22
# Receba 2 valores inteiros e diferentes.
# Mostre os valores em ordem crescente.

# Declarar variáveis globais
valor1 = 0
valor2 = 0


def mostrar_ordem():
    global valor1, valor2

    # Processamento e resultado
    if valor1 < valor2:
        print(valor1, valor2)
    else:
        print(valor2, valor1)


def main():
    global valor1, valor2

    # Entrada de dados
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    mostrar_ordem()


main()