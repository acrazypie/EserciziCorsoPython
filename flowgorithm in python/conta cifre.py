numero = int(input("Inserisci un numero: "))
numero = abs(numero)

cifre = 1
while numero >= 10:
    numero //= 10
    cifre += 1

print(f"Il numero ha {cifre} cifre.")
