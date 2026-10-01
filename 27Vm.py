# Calcule a velocidade média em km/h.


def calcular_velocidade(voltas, extensao, tempo):
    # Processamento
    distancia = voltas * extensao

    # Converter metros para quilômetros
    distancia = distancia / 1000

    # Calcular velocidade em km/h
    velocidade = distancia / (tempo / 60)

    # Mostrar resultado
    print("Velocidade média:", velocidade, "km/h")


def main():
    # Entrada de dados
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite o tempo em minutos: "))

    calcular_velocidade(voltas, extensao, tempo)


main()