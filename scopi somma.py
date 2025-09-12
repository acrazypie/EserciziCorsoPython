num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
num3 = int(input("Inserisci il terzo numero: "))


def somma():
    somma = num1 + num2 + num3
    print(f"La somma parziale è: {somma}")
    num4 = int(input("Inserisci un altro numero da sommare: "))
    return num4


totale = somma() + num1 + num2 + num3
print("La somma totale è:", totale)
