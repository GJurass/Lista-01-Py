one = int(input("Digite a quantidade de moedas de 1 centavo:\n"))
five = int(input("Digite a quantidade de moedas de 5 centavos:\n"))
ten = int(input("Digite a quantidade de moedas de 10 centavos:\n"))
tfive = int(input("Digite a quantidade de moedas de 25 centavos:\n"))
fifth = int(input("Digite a quantidade de moedas de 50 centavos:\n"))
real = int(input("Digite a quantidade de moedas de 1 real:\n"))

vone = one * 1
vfive = five * 5
vten = ten * 10
vtfive = tfive * 25
vfifth = fifth * 50
vreal = real * 100

total = (vone + vfive + vten + vtfive + vfifth + vreal) / 100

print(f"O valor total economizado por Pedrinho sera de R${total:.2f}")