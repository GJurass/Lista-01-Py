dias = int(input("Quantos dias sem acidentes?\n"))
meses = float(dias/30)
anos = float(meses/12)

if meses < 12:
    print("\nEstamos a",round(meses,2),"meses sem acidentes")
if anos >= 1:
    print("\nEstamos a",round(anos,2),"anos sem acidentes")
