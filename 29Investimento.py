# Calcule o valor corrigido em 30 dias.


def calcular_investimento(tipo, valor):
    # Processamento
    if tipo == 1:
        valor_corrigido = valor * 1.03
        print("Valor corrigido:", valor_corrigido)

    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print("Valor corrigido:", valor_corrigido)

    else:
        print("Tipo de investimento inválido.")


def main():
    # Entrada de dados
    tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
    valor = float(input("Digite o valor do investimento: "))

    calcular_investimento(tipo, valor)


main()