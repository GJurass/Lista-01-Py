def decompor_numero(numero):
    if not (0 <= numero <= 999):
        print("Por favor, insira um número inteiro de até três dígitos.")
        return

    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    print(f"CENTENA = {centena}")
    print(f"DEZENA = {dezena}")
    print(f"UNIDADE = {unidade}")

numero = int(input("Digite um número inteiro de até três dígitos:\n"))
decompor_numero(numero)