def calcola_operazione(a, b, operazione):
    if operazione == "somma":
        return a + b
    elif operazione == "sottrai":
        return abs(a - b)
    else:
        return "Operazione non valida"


# Main
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (somma, sottrai): ")

risultato = calcola_operazione(a, b, operazione)
print(f"Il risultato di {operazione} tra {a} e {b} è: {risultato}")
