n = int(input("Inserisci la lungezza > 2: "))

while n < 2:
    n = int(input("Errore! Inserisci la lungezza > 2: "))
vettore = []

for i in range(0, n):
    vettore.append(int(input(f"Numero {i+1}: ")))

mindiff = abs(vettore[1] - vettore[0])
num1 = vettore[0]
num2 = vettore[1]

for i in range(0, n - 2):
    diff = abs(vettore[i] - vettore[i + 1])
    if diff < mindiff:
        mindiff = diff
        num1 = vettore[i]
        num2 = vettore[i + 1]

print(
    f"I numeri con la differenza minima sono {num1} e {num2} con una differenza di {mindiff}"
)
