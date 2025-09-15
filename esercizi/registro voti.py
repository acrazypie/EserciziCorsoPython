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


def aggiungi_studente(
    reg: dict, id: str, nome: str, cognome: str, classe: int, corso: str
) -> bool:
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


def aggiungi_materia(reg: dict, id: str, materia: str) -> bool:
    if id not in reg:
        return False
    if materia not in reg[id]["voti"]:
        reg[id]["voti"][materia] = []
    return True


def aggiungi_voti(reg: dict, id: str, materia: str, *voto: float) -> bool:
    if id not in reg or materia not in reg[id]["voti"]:
        return False
    for v in voto:
        if not (0 <= v <= 10):
            return False
        reg[id]["voti"][materia].append(round(v, 2))
    return True


def media_studente(reg: dict, id: str) -> float | None:
    if id not in reg:
        return None
    voti = [voto for materie in reg[id]["voti"].values() for voto in materie]
    return round(sum(voti) / len(voti), 2) if voti else 0.0


def media_materia_studente(reg: dict, id: str, materia: str) -> float | None:
    if id not in reg or materia not in reg[id]["voti"]:
        return None
    voti = reg[id]["voti"][materia]
    return round(sum(voti) / len(voti), 2) if voti else 0.0


def pagella(reg: dict, id: str) -> dict[str, float] | None:
    if id not in reg:
        return None
    voti = reg[id]["voti"]
    if not voti:
        return None
    pagella_dict = {}
    for materia in voti:
        media = media_materia_studente(reg, id, materia)
        if media is not None:
            pagella_dict[materia] = media
    return pagella_dict


def bocciabili(reg: dict, soglia=6.0) -> list[str]:
    bocciati = []
    for id, info in reg.items():
        for materia, voti in info["voti"].items():
            if voti and (sum(voti) / len(voti)) < soglia:
                bocciati.append(id)
                break
    return bocciati


def top_studente(reg: dict) -> tuple[str, float] | None:
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


print("----------------------------")
print("Aggiungi studente:", aggiungi_studente(registro, "s6", "Anna", "Verdi", 5, "A"))
print("---------------------------")
print("Aggiungi materia:", aggiungi_materia(registro, "s6", "Italiano"))
print("---------------------------")
print("Aggiungi voti:", aggiungi_voti(registro, "s6", "Italiano", 8, 7.5, 9))
print("---------------------------")
print("Media studente:", media_studente(registro, "s6"))
print("---------------------------")
print("Media di Italiano:", media_materia_studente(registro, "s6", "Italiano"))
print("---------------------------")
print("Pagella:", pagella(registro, "s6"))
print("---------------------------")
print("Bocciabili:", bocciabili(registro))
print("---------------------------")
print("Top studente:", top_studente(registro))
