paes = int(input("Quantos paes foram vendidos?\n"))
broas = int(input("Quantas broas foram vendidos?\n"))

v_paes = paes * 0.12
v_broas = broas * 1.50

total = v_paes + v_broas

poup = total * 0.1

print("O valor total das vendas foi de ", total,"R$\nE o valor a ser guardado é de ", poup,"R$")