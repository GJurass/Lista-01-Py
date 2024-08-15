p1 = float(input("Qual a nota da prova 1?\n"))
p2 = float(input("Qual a nota da prova 2?\n"))
p3 = float(input("Qual a nota da prova 3?\n"))

mp2 = p2 * 2
mp3 = p3 * 3

mt = p1 + mp2 + mp3

mp = p1 + p2 + p3

mf = mt / mp

print("\nA média final será de:", mf)
