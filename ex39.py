sali = float(input("Digite o valor do salario:\n"))
mult1 = float(input("Digite o valor da primeira conta:\n"))
mult2 = float(input("Digite o valor da segunda conta:\n"))
porc1 = float(input("Digite a porcentagem da primeira multa:\n"))
porc2 = float(input("Digite a porcentagem da segunda multa:\n"))

t1 = mult1 + (mult1 * (porc1 / 100))
t2 = mult2 + (mult2 * (porc2 / 100))

tsal = sali - (t1 + t2)

print(f"Apos pagamento das contas restaram R${tsal:.2f}")
