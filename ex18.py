horas = float(input("Informe o total de horas normais trabalhadas\n"))
horasex = float(input("Informe o total de horas extras trabalhadas\n"))

vhoras = horas * 10
vhorasex = horasex * 15

salb = vhoras + vhorasex
sall = salb * 0.9

print(f"O salario bruto sera de R${salb:.2f} enquanto o liquido sera de R${sall:.2f}")