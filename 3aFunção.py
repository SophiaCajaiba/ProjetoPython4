def calcular_fatorial(numero):
    # Declarar variável local
    fatorial = 1

    # Processamento
    for contador in range(1, numero + 1):
        fatorial = fatorial * contador

    # Retornar resultado
    return fatorial


def main():
    # Entrada de dados
    numero = int(input("Digite um número inteiro: "))

    # Chamar função
    resultado = calcular_fatorial(numero)

    # Mostrar resultado
    print("Fatorial:", resultado)


main()