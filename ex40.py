import math

cat1 = float(input("Digite o valor do primeiro cateto:\n"))
cat2 = float(input("Digite o valor do segundo cateto:\n"))

soma_quadrados = cat1**2 + cat2**2

hip = math.sqrt(soma_quadrados)

print(f"A hipotenusa do triângulo é igual a {hip:.2f}")
