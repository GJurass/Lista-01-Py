num = int(input("Digite o numero que deseja a tabuada:\n"))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")