salf = float(input("Digite o salario fixo:\n"))
vendas = float(input("Digite o valor de vendas:\n"))

cmss = vendas * 0.04
salb = salf + cmss

print(f"O valor da comissao sera de R${cmss:.2f} e o salario bruto de R${salb:.2f}")