try:
    num1 = float(input("Scegli il primo numero: "))
    num2 = float(input("Scegli il secondo numero: "))
    risultato = num1 / num2
    print("Il risultato è:", risultato)
except ValueError:
    print("Errore: Input non valido. Assicurati di inserire numeri.")
except ZeroDivisionError:
    print("Errore: Divisione per zero non permessa.")
except Exception as e:
    print(f"Errore inaspettato: {e}")
else:
    print("Operazione completata con successo.")
finally:
    print("Operazione terminata.")
