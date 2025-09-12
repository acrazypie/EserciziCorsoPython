"""
Registro voti scolastico.
Crea la voce se non esiste. Ritorna True se creato, False se già presente.

- aggiungi_studente(reg, id, nome, cognome, classe, corso) -> bool
- aggiungi_materia(reg, id, materia) -> bool (crea lista se non c’è)
- aggiungi_voto(reg, id, materia, voto: float) -> bool (0–10, arrotonda a 2 cifre decimali)
- media_studente(reg, id) -> float | None (tutte le materie)
- media_materia_studente(reg, id, materia) -> float | None
- pagella(reg, id) -> dict[str, float] | None (materia → media)
- bocciabili(reg, soglia=6.0) -> list[str] (almeno una materia < soglia)
- top_student(reg) -> tuple[str, float] | None
"""

registro = {
    "s1": {
        "nome": "Luca",
        "cognome": "Sgargi",
        "classe": 5,
        "corso": "A",
        "voti": {"Italiano": [7.5, 6, 9]},
    },
    "s2": {
        "nome": "Marta",
        "cognome": "Rossi",
        "classe": 5,
        "corso": "A",
        "voti": {"Matematica": [8, 7, 6]},
    },
    "s3": {
        "nome": "Giovanni",
        "cognome": "Bianchi",
        "classe": 5,
        "corso": "A",
        "voti": {"Storia": [6, 5, 7]},
    },
    "s4": {
        "nome": "Elena",
        "cognome": "Verdi",
        "classe": 5,
        "corso": "A",
        "voti": {"Inglese": [9, 8, 10]},
    },
    "s5": {
        "nome": "Marco",
        "cognome": "Neri",
        "classe": 5,
        "corso": "A",
        "voti": {"Scienze": [7, 6, 8]},
    },
}


def aggiungi_studente(reg, id, nome, cognome, classe, corso) -> bool:
    if id in reg:
        return False
    reg[id] = {
        "nome": nome,
        "cognome": cognome,
        "classe": classe,
        "corso": corso,
        "voti": {},
    }
    return True


def aggiungi_materia(reg, id, materia) -> bool:
    if id not in reg:
        return False
    if materia not in reg[id]["voti"]:
        reg[id]["voti"][materia] = []
    return True


def aggiungi_voto(reg, id, materia, voto: float) -> bool:
    if id not in reg or materia not in reg[id]["voti"] or not (0 <= voto <= 10):
        return False
    reg[id]["voti"][materia].append(round(voto, 2))
    return True


def media_studente(reg, id) -> float | None:
    if id not in reg:
        return None
    voti = [voto for materie in reg[id]["voti"].values() for voto in materie]
    return round(sum(voti) / len(voti), 2) if voti else 0.0


def media_materia_studente(reg, id, materia) -> float | None:
    if id not in reg or materia not in reg[id]["voti"]:
        return None
    voti = reg[id]["voti"][materia]
    return round(sum(voti) / len(voti), 2) if voti else 0.0


def pagella(reg, id) -> dict[str, float] | None:
    if id not in reg:
        return None
    materia: str = reg[id]["voti"][0] if reg[id]["voti"] else ""
    if materia == "":
        return None
    media = media_materia_studente(reg, id, materia)
    return {materia: media} if media is not None else None


def bocciabili(reg, soglia=6.0) -> list[str]:
    bocciati = []
    for id, info in reg.items():
        for materia, voti in info["voti"].items():
            if voti and (sum(voti) / len(voti)) < soglia:
                bocciati.append(id)
                break
    return bocciati


def top_studente(reg) -> tuple[str, float] | None:
    if not reg:
        return None
    top_id: str = ""
    top_media: float = -1.0
    for id, studente in reg.items():
        media = media_studente(reg, id)
        if media is not None and media > top_media:
            top_id = id
            top_media = media
    return (top_id, top_media) if top_id else None
