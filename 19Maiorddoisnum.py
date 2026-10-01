# Declarar variáveis globais
valor1 = 0
valor2 = 0
resultado = 0


def calcular_diferenca():
    global valor1, valor2, resultado

    # Processamento
    if valor1 > valor2:
        resultado = valor1 - valor2
    else:
        resultado = valor2 - valor1

    # Mostrar resultado
    print("Diferença:", resultado)


def main():
    global valor1, valor2

    # Entrada de dados
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    calcular_diferenca()


main()