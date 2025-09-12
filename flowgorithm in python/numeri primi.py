def e_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


limite = int(input("Inserisci un numero: "))

print(f"Numeri primi tra 1 e {limite}:")

for numero in range(2, limite + 1):
    if e_primo(numero):
        print(numero, end=" ")