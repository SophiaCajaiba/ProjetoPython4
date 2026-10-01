# Declarar variáveis globais
numero = 0


def verificar_divisibilidade():
    global numero

    # Processamento
    if numero % 2 == 0 and numero % 3 == 0:
        print("É divisível por 2 e 3.")
    elif numero % 2 == 0:
        print("É divisível somente por 2.")
    elif numero % 3 == 0:
        print("É divisível somente por 3.")
    else:
        print("Não é divisível por 2 nem por 3.")


def main():
    global numero

    # Entrada de dados
    numero = int(input("Digite um número inteiro: "))

    verificar_divisibilidade()


main()