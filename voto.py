"""
Data una lista di record di voti utente es votiStudenti = [("Mario", "Rossi", 4,6,7,6,8 "Da controllare"), ("Luca","Bianchi", 9,2,3,9 "Non controllare"), ]
nel caso in cui la tupla voto cotenga la strigna "Da controllare" andiamo a stampare a schermo il voto minimo,
il voto massimo e nel caso in cui abbia piu' di 2 voti inferiori al 6 stampare il nome dello studente con la scritta "In pericolo di bocciatura"
"""

votiStudenti = [
    ("Mario", "Rossi", 4, 6, 7, 6, 8, "Da controllare"),
    ("Luca", "Bianchi", 9, 2, 3, 9, "Non controllare"),
    ("Giulia", "Verdi", 8, 7, 9, 6, 10, "Da controllare"),
    ("Anna", "Neri", 5, 4, 6, 5, "Da controllare"),
    ("Paolo", "Gialli", 7, 8, 9, 10, "Non controllare"),
]

for record in votiStudenti:
    nome, cognome, *voti, stato = record
    if stato == "Da controllare":
        print(f"----- {nome} {cognome} -------")

        voto_minimo = min(voti)
        voto_massimo = max(voti)
        print(f"Voto Minimo: {voto_minimo}")
        print(f"Voto Massimo: {voto_massimo}")

        voti_bassi = 0
        for voto in voti:
            if voto < 6:
                voti_bassi += 1

        if voti_bassi > 2:
            print(f"In pericolo di bocciatura")
