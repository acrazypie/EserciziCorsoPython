n = int(input("Inserisci un numero: "))

print(f"I primi 10 multipli di {n} sono:")

for i in range(1, 11):
    m = n * i
    print(f"{n} x {i} = {m}")