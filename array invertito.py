# --- split(sep, maxsplit) -> separa la stringa in pezzi
# sep -> il separatore per dividere, usa gli spazi vuoti se non non usato
# maxsplit -> numero massimo di separazioni da sinistra, -1 per infinito di default
array = input("Inserisci gli elementi dell'array separati da spazi: ").split()

# --- lista[inizio:fine:passo]
# inizio -> dove inizia, dall'inizio se vuoto
# fine -> dove finisce, fino alla fine se vuoto
# passo -> di quanto avanza all'interno della lista, -1 va al contrario nell'array
array_invertito = array[::-1]

print("Array originale:", array)
print("Array invertito:", array_invertito)
