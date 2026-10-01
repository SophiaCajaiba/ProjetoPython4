# Exercício 23
# Receba 3 valores em ordem crescente e um quarto valor.
# Mostre os 4 valores em ordem crescente.

# Declarar variáveis globais
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0


def mostrar_ordem():
    global valor1, valor2, valor3, valor4

    # Processamento
    valores = [valor1, valor2, valor3, valor4]
    valores.sort()

    # Mostrar resultado
    print("Valores em ordem crescente:")
    print(valores)


def main():
    global valor1, valor2, valor3, valor4

    # Entrada de dados
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))
    valor4 = int(input("Digite o quarto valor: "))

    mostrar_ordem()


main()