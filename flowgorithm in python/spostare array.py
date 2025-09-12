array = input("Inserisci gli elementi dell'array separati da spazi: ").split()

temp = array[len(array)-1]

for num in array:
    array[array.index(num)] = temp
    temp = array[array.index(num)+1]
