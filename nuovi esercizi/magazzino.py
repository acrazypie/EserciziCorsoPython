magazzino = {
    "product_HHJ23": {"nome": "penna", "quantita": 20, "prezzo": 1.5},
    "product_HZX24": {"nome": "matita", "quantita": 30, "prezzo": 1.0},
    "product_JJA34": {"nome": "gomma", "quantita": 15, "prezzo": 0.5},
    "product_KKL45": {"nome": "righello", "quantita": 10, "prezzo": 2.0},
    "product_LLM56": {"nome": "quaderno", "quantita": 25, "prezzo": 3.0},
}


def stampa_info_prodotto(codice_prodotto: str):
    if codice_prodotto in magazzino:
        prodotto = magazzino[codice_prodotto]
        nome = prodotto["nome"]
        quantita = prodotto["quantita"]
        prezzo = prodotto["prezzo"]
        print(
            f"Codice: {codice_prodotto} - Nome: {nome} - Quantità: {quantita} - Prezzo: {prezzo} €"
        )
    else:
        print("Prodotto non trovato.")


def totale_valore_magazzino() -> float:
    totale = 0.0
    for prodotto in magazzino.values():
        totale += prodotto["quantita"] * prodotto["prezzo"]
    return totale


stampa_info_prodotto("product_JJA34")
print(totale_valore_magazzino())
