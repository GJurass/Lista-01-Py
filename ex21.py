lata = int(input("Digite a quantidade de latas compradas\n"))
g600 = int(input("Digite a quantidade de garrafas de 600ml compradas\n"))
g2000 = int(input("Digite a quantidade de garrafas de 2l compradas\n"))

vlata = lata * 350
vg600 = g600 * 600
vg2000 = g2000 * 2000

vtotal = (vlata + vg600 + vg2000) / 1000

print(f"Serao comprados {vtotal} litros de refrigerante.")