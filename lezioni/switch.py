"""
Descrizione: Scrivi un programma che chieda all'utente due numeri e un'operazione (+, -, *, /)
le varie operazioni vengono effettuate da funzioni diverse es somma(val1,val2) e ne ritorni il risultato ecc.
Esegui l'operazione e stampa il risultato.
"""

num1 = float(input("Scegli il primo numero: "))
num2 = float(input("Scegli il secondo numero: "))
operazione = input("Scegli l'operazione (+, -, *, /): ")


def somma(val1, val2):
    return val1 + val2


def sottrazione(val1, val2):
    return val1 - val2


def moltiplicazione(val1, val2):
    return val1 * val2


def divisione(val1, val2):
    return val1 / val2 if val2 != 0 else "Errore: Divisione per zero"


def default(val1, val2):
    return f"Operazione non valida con i valori {val1} e {val2}"


# if-elif-else
if operazione == "+":
    risultato = somma(num1, num2)
elif operazione == "-":
    risultato = sottrazione(num1, num2)
elif operazione == "*":
    risultato = moltiplicazione(num1, num2)
elif operazione == "/":
    risultato = divisione(num1, num2)
else:
    risultato = default(num1, num2)

# match
match operazione:
    case "+":
        risultato = somma(num1, num2)
    case "-":
        risultato = sottrazione(num1, num2)
    case "*":
        risultato = moltiplicazione(num1, num2)
    case "/":
        risultato = divisione(num1, num2)
    case _:
        risultato = default(num1, num2)

# dizionario
operazioni = {"+": somma, "-": sottrazione, "*": moltiplicazione, "/": divisione}
risultato = operazioni.get(operazione, default)(num1, num2)

print("Il risultato è:", risultato)
