import math

h = float(input("Digite a altura do cilindro:\n"))
b = float(input("Digite o raio da base do cilindro:\n"))

v = (math.pi * pow(b, 2)) * h

print(f"O volume do cilindro sera de: {v:.2f} cm\u00b3")