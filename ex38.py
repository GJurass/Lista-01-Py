from datetime import date

anoatual = date.today().year
anonasc = int(input("Digite o ano de nascimento\n"))
idade = anoatual - anonasc
idadem = idade * 12
idaded = idade * 365
idades = idade * 52

print(f"Uma pessoa nascida em {anonasc} hoje tem {idade} anos, {idadem} meses, {idades} semanas e {idaded} dias de vida.")
