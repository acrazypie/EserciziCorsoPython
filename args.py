def somma(*numeri, moltiplicatore=1) -> int:
    for n in numeri:
        if not isinstance(n, int):
            raise ValueError("Tutti gli argomenti devono essere interi.")
    return sum(numeri) * moltiplicatore


def sottrazione(a: int, b: int, /) -> int:
    return abs(a - b)


print(somma(1, 2, 3))
print(somma(1, 2, 3, moltiplicatore=2))
print(sottrazione(5, 3))
sottrazione(5, a=3)  # Questo genererà un errore
