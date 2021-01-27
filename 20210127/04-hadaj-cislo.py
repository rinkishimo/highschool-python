import random


def generuj_hru(od, do):
    a, b = 0, 0
    while b - a < 1:
        a = random.randint(od, do)
        b = random.randint(od, do)
        a, b = min(a, b), max(a, b)
    c = random.randint(a, b)
    return a, b, c


a, b, tajne_cislo = generuj_hru(1, 1000)
print()
print(f"ahoj, myslim si cislo od {a} do {b}. hadaj ake?")

pocet_hadani = 0
while True:
    cislo = input("tvoj tip: ")
    if cislo.strip() == "":
        vstup = input("oo, uz ta to nebavi a chces skoncit? [a/N] ")
        if vstup.strip().lower() == "a":
            print(f"ok, chapem. myslel som si {tajne_cislo}.")
            break
        else:
            continue

    if not cislo.isdigit():
        print("toto predsa nie je cislo ;)")
        continue

    pocet_hadani += 1
    tip = int(cislo)

    if tip < a or tip > b:
        print(f"hehehe, povedal som, ze je od {a} do {b}. skus znova.")
    elif tip > tajne_cislo:
        print("ee, moje cislo je mensie.")
    elif tip < tajne_cislo:
        print(f"oo, moje cislo je vacsie.")
    elif tip == tajne_cislo:
        print(f"BINGO, {tip} je moje cislo. uhadol si to na {pocet_hadani} pokusov.")
        break

print("tak ahoj...")
print()
