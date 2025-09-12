array = [int(x) for x in input("Inserisci gli elementi dell'array separati da spazi: ").split()]

for (index, value) in enumerate(array):
    if index == len(array) - 1:
        break
    diff = array[index+1] - array[index]
    print(diff)
