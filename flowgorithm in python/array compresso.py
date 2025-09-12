array = [int(x) for x in input("Inserisci gli elementi dell'array separati da spazi: ").split()]

for num in array:
    if array.count(num) > 1:
        array.remove(num)

print(array)