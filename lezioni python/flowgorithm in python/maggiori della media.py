def conta_maggiori_della_media(arr):
        if not arr:
            return 0
        media = sum(arr) / len(arr)
        count = sum(1 for x in arr if x > media)
        return f"{count} numeri sono maggiori della media {media}." if count > 1 else f"{count} oof sad"


numeri = [int(x) for x in input("Inserisci gli elementi dell'array separati da spazi: ").split()]
print(conta_maggiori_della_media(numeri))
