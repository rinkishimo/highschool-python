import random


def generuj_priklad(do_kolko):
    a = random.randint(0, do_kolko)
    b = random.randint(0, do_kolko)
    while a + b > do_kolko:
        b = random.randint(0, int(b / 2))
    return f"{a} + {b} =", str(a + b)


pocet_prikladov = int(input("kolko chces prikladov? "))
maximalne_cislo = int(input("do kolko vies pocitat? "))
dobre = 0

for i in range(pocet_prikladov):
    priklad, spravny_vysledok = generuj_priklad(maximalne_cislo)
    vysledok = input(f"{i}:  {priklad}").strip()  # vypytat si vysledok
    if vysledok == spravny_vysledok:
        dobre += 1

# vypisat vysledky
print(
    f"Mas dobrych {dobre} z {pocet_prikladov}, co je {(dobre / pocet_prikladov * 100):.2f}%."
)
