# Calcular:
# 1 + 1/1! + 1/2! + ... + 1/N!


def calcular_fatorial(numero):
    # Declarar variável local
    fatorial = 1

    # Processamento
    for contador in range(1, numero + 1):
        fatorial = fatorial * contador

    # Retornar resultado
    return fatorial


def calcular_divisao(numero1, numero2):
    # Retornar a divisão
    return numero1 / numero2


def main():
    # Entrada de dados
    n = int(input("Digite o valor de N: "))

    soma = 1

    # Calcular a série
    for contador in range(1, n + 1):
        fatorial = calcular_fatorial(contador)
        resultado = calcular_divisao(1, fatorial)
        soma = soma + resultado

    # Mostrar resultado
    print("Resultado da série:", soma)


main()