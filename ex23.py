sombras = float(input("Digite o comprimento da sua sombra em cm:\n"))
sombrap = float(input("Digite o comprimento da sombra do predio em cm:\n"))
altura = float(input("Digite sua altura em cm:\n"))

msombras = sombrap / sombras
alturap = msombras * altura
alturam = alturap / 100

print(f"O predio tera {alturam:.2f}m de altura")