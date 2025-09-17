x = int(input())
y = int(input())

s = x + y
d = x - y
m = x * y
D = x / y
Dr = x % y

max = x if x > y else y

min = x if x < y else y

print("La somma vale " + str(s))
print("La differenza vale " + str(d))
print("La moltiplicazione vale " + str(m))
print("La divisione vale " + str(D))
print("Il resto della divisione vale " + str(Dr))
print("Il numero piu alto vale " + str(max))
print("Il numero piu basso vale " + str(min))
