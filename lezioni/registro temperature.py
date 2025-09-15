"""
Gestisci un registro temperature: ogni città ha una lista di temperature giornaliere in °C (float).
Implementa:

aggiungi_citta(m, nome) -> bool — crea la chiave se non esiste.

aggiungi_temp(m, nome, t) -> bool — aggiunge una temperatura t se la città esiste e -50 ≤ t ≤ 60. Arrot. a 1 decimale.

stats_citta(m, nome) -> tuple[float, float, float] | None — ritorna (min, max, media) con 1 decimale; None se non ha dati.

piu_calde_di(m, soglia) -> list[str] — città con media > soglia.

estremi_globali(m) -> tuple[tuple[str,float], tuple[str,float]] | None — ritorna ((città_min, valore_min), (città_max, valore_max)), oppure None se non ci sono dati.
"""

meteo = {
    "Palermo": [24.5, 25.2, 26.0],
    "Agrigento": [23.0, 24.1],
}


def aggiungi_citta(m: dict, nome: str) -> bool:
    if nome not in m:
        m[nome] = []
        return True
    return False


def aggiungi_temp(m: dict, nome: str, t: float) -> bool:
    if nome in m and -50 <= t <= 60:
        m[nome].append(round(t, 1))
        return True
    return False


def stats_citta(m: dict, nome: str) -> tuple[float, float, float] | None:
    if nome not in m or not m[nome]:
        return None
    temps = m[nome]
    minimo = round(min(temps), 1)
    massimo = round(max(temps), 1)
    media = round(sum(temps) / len(temps), 1)
    return (minimo, massimo, media)


def piu_calde_di(m: dict, soglia: float) -> list[str]:
    calde = []
    for nome, temps in m.items():
        if temps:
            media = sum(temps) / len(temps)
            if media > soglia:
                calde.append(nome)
    return calde


def estremi_globali(m: dict) -> tuple[tuple[str, float], tuple[str, float]] | None:
    min_citta = None
    min_valore = float("inf")
    max_citta = None
    max_valore = float("-inf")

    for nome, temps in m.items():
        if temps:
            citta_min = min(temps)
            citta_max = max(temps)

            if citta_min < min_valore:
                min_valore = citta_min
                min_citta = nome

            if citta_max > max_valore:
                max_valore = citta_max
                max_citta = nome

    if min_citta is None or max_citta is None:
        return None

    return ((min_citta, round(min_valore, 1)), (max_citta, round(max_valore, 1)))


print(aggiungi_citta(meteo, "Catania"))
print(aggiungi_temp(meteo, "Catania", 25.3))
print(aggiungi_temp(meteo, "Catania", 27.8))
print(aggiungi_temp(meteo, "Catania", 30.0))
print(stats_citta(meteo, "Catania"))
print(piu_calde_di(meteo, 25.0))
print(estremi_globali(meteo))
