def print_item(item: tuple[str, float, int], sconto=False):
    nome = item[0]
    tot = tot_item(item, sconto)
    print(f"Totale {nome} -> {tot}")


def tot_item(item: tuple[str, float, int], sconto=False):
    nome, prezzo, quantita = item
    totale = prezzo * quantita
    if sconto and nome != "latte":
        totale *= 0.8  # Applica uno sconto del 20% sul latte
    return totale


def tot_cart(cart: list[tuple[str, float, int]]):
    totale = 0
    for item in cart:
        totale += tot_item(item)
    print(f"TOTALE CARRELLO = {totale}")


def find_item(cart: list[tuple[str, float, int]], nome: str):
    for item in cart:
        if item[0] == nome:
            return f"TROVATO -> {item[0]} | {item[1]} | {item[2]}"
    return f"NON HO TROVATO -> {nome}"


def change_quantity(cart: list[tuple[str, float, int]], nome: str, nuova_quantita: int):
    for i in range(len(cart)):
        if cart[i][0] == nome:
            cart[i] = (cart[i][0], cart[i][1], nuova_quantita)
            return f"QUANTITÀ AGGIORNATA -> {cart[i][0]} | {cart[i][1]} | {cart[i][2]}"
    return f"NON HO TROVATO -> {nome}"


# -------------- ESEMPI --------------
carrello = [("mele", 2.5, 3), ("banane", 1.8, 4), ("arance", 3.0, 1), ("latte", 1.2, 2)]


print_item(carrello[0], sconto=False)
print_item(carrello[1], sconto=True)
print_item(carrello[2], sconto=False)
print_item(carrello[3], sconto=True)  # Sconto non applicato sul latte

tot_cart(carrello)

print(find_item(carrello, "banane"))

print(change_quantity(carrello, "arance", 5))
tot_cart(carrello)
# -----------------------------------
