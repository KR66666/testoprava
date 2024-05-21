import random 

kol = random.randint(1,15)
body = 0
zivoty = 2
otazky = kol/2

for k in range(kol):
    pole = []

    delka = random.randint(1,10)

    for t in range(delka):
        pole.append(random.randint(1,13))

    print(pole)

    a = int(input("Zadejte delku: "))

    if a == delka:
       print(f"To je spravně: {a}")
       body = body + 1
       print(f"Mate +{body} bod")
    else:
       print(f"Špatně, a to je spravně: {delka}")

print(f"Kol měli: {kol}")
print(f"Bodu měli: {body}")

if body < otazky:
    zivoty = zivoty - 1
    print(f"Stratili {zivoty} zivot")
else:
    print(f"Mate {zivoty} zivoty")