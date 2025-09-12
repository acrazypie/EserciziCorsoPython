b1 = float(input("Inserire la base del primo triangolo-> "))
h1 = float(input("Inserire la altezza del primo triangolo-> "))
b2 = float(input("Inserire la base del secondo triangolo-> "))
h2 = float(input("Inserire la altezza del secondo triangolo-> "))

a1 = (b1 * h1) / 2
a2 = (b2 * h2) / 2

if a1 == a2:
    print("Le aree sono uguali")
elif a1 > a2:
    print("Il primo triangolo ha l'area maggiore")
else:
    print("Il secondo triangolo ha l'area maggiore")
