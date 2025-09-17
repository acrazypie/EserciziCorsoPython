"""
Scrivi un programma che :
1) Chiede una frase non vuota (ricontinua finchè l'utente non scrive qualcosa )
2) Estrae le parole.
3) Stampa la frase con le parole in ordine inverso.
4) Stampa :
  - quante parole ci sono
  - quante parole hanno più di 4 caratteri
  - l' elenco numerato delle parole lunghe
  - la parola più lunga
"""

frase = input("Inserisci una frase: ")
while not frase:
    frase = input("Frase vuota, riprova: ")

parole = frase.split()
print("Frase invertita:", " ".join(parole[::-1]))

print("Numero di parole:", len(parole))

parole_lunghe = [p for p in parole if len(p) > 4]
print("Numero di parole lunghe:", len(parole_lunghe))

print("Elenco delle parole lunghe:")
for i, p in enumerate(parole_lunghe, 1):
    print(f"{i}. {p}")

print("Parola più lunga:", max(parole, key=len))
