import random

min_cislo = 1
max_cislo = 30
pocet_cisel = 5


def nacitaj_tip():
    dobre = False
    cisla = []

    while not dobre:
        cisla = []
        vstup = input(f"Zadaj svoj tip ({pocet_cisel} cisel oddelenych medzerami): ")
        casti = vstup.strip().split(" ")
        for cast in casti:
            cislo = int(cast)
            if cislo not in cisla:
                cisla.append(cislo)

        # overenie spravnosti
        dobre = True
        if len(cisla) != pocet_cisel:
            print(f"- Cisel ma byt presne {pocet_cisel} a nesmu sa opakovat!")
            dobre = False

        for cislo in cisla:
            if cislo < min_cislo or cislo > max_cislo:
                print(f"- Cislo musi byt z rozsahu {min_cislo} az {max_cislo}!")
                dobre = False
                break

    cisla.sort()
    return cisla


def vylosuj_cisla():
    cisla = []
    while len(cisla) < pocet_cisel:
        cislo = random.randint(min_cislo, max_cislo)
        if cislo not in cisla:
            cisla.append(cislo)
    cisla.sort()
    return cisla


def over_tip(tcisla, vcisla):
    vylosovane = []
    for vc in vcisla:
        vylosovane.append(str(vc))

    uhadnute = []
    for tip in tcisla:
        if tip in vcisla:
            uhadnute.append(str(tip))

    print(f"Vylosovane boli tieo cisla: {', '.join(vylosovane)}.")
    print(f"Uhadli ste {len(uhadnute)} cisel.")
    if len(uhadnute) > 0:
        print(f"Konkretne tieto: {', '.join(uhadnute)}.")
    else:
        print("Smola :P")


# vypytat tip od uzivatela => [11, 2, 30, 4, 6]
tipnute = nacitaj_tip()

# vylosuj cisla
vylosovane = vylosuj_cisla()

# porovnaj tip s vylosovanymi a vypis vysledok
over_tip(tipnute, vylosovane)
