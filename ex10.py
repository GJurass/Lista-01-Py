import math


def calcular_distancia(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1

    soma_quadrados = delta_x ** 2 + delta_y ** 2

    distancia = math.sqrt(soma_quadrados)

    return distancia


print("Digite as coordenadas do primeiro ponto (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Digite as coordenadas do segundo ponto (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = calcular_distancia(x1, y1, x2, y2)

print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {distancia:.2f}")
