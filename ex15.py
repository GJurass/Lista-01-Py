total = float(input("Digite o valor total da conta:\n"))

part = total // 3
rest = total - (part * 2)

print(f"\nCarlos e Andre pagarao R${int(part)} cada um e Felipe pagara R${int(rest)}.")