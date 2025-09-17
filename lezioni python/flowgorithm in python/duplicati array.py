array = list(
    map(int, input("Inserisci gli elementi dell'array separati da spazi: ").split())
)

duplicates = list(set([x for x in array if array.count(x) > 1]))
print(duplicates)

# ------------------------------------------------------

arr = [1, 2, 3, 4, 2, 7, 8, 1, 3, 3]

visti = set()
duplicati = set()

for num in arr:
    if num in visti:
        duplicati.add(num)
    else:
        visti.add(num)

print(list(duplicati))
