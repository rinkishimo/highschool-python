POCET_VEZI = 3
MAX_DISK = 100
PRIKAZ_KONIEC = -100


def vytvorVeze(pocet_poschodi):
    veze = "987654321"[-pocet_poschodi::]
    veze += "-" * (POCET_VEZI - 1)
    return veze


def vypisVeze(stav_vezi):
    print()
    veze = stav_vezi.split("-")
    for i in range(len(veze)):
        print(i + 1, ":", veze[i])
    print()
    return None

def xprint(s):
    print(s, end='')
    return None

def vypisVeze2(stav_vezi):
    print()
    veze = stav_vezi.split("-")
    vyska = 0
    najvacsi_disk = 0
    for i in range(len(veze)):
        vyska = len(veze[i]) if vyska < len(veze[i]) else vyska
        for x in veze[i]:
            najvacsi_disk = int(x) if int(x) > najvacsi_disk else najvacsi_disk 

    max_sirka_disku = 1 + 2 * najvacsi_disk

    for r in range(0, vyska + 1):
        for i in range(len(veze)):
            if len(veze[i]) > vyska - r:
                sirka_disku = 1 + 2 * int(veze[i][vyska - r])
                xprint(' ' * ((max_sirka_disku - sirka_disku) // 2))
                xprint('*' * (sirka_disku))
                xprint(' ' * ((max_sirka_disku - sirka_disku) // 2))
            else:
                xprint(' ' * ((max_sirka_disku - 1) // 2))
                xprint('|' * (1))
                xprint(' ' * ((max_sirka_disku - 1) // 2))
            xprint('   ')
        xprint('\n')
    print()
    # print(stav_vezi)
    # print()
    return None

def presun(stav_vezi, z, na):
    # print(f"Presun z {z + 1} na {na + 1}...")
    if (z < 0 or z >= POCET_VEZI) or (na < 0 or na >= POCET_VEZI) or (z == na):
        print("Z alebo NA nie je dobre.")
        return stav_vezi
    veze = stav_vezi.split("-")
    z_veza = veze[z]
    if len(z_veza) == 0:
        print("Pokus o presun z prazdnej veze.")
        return stav_vezi

    # kontrola, ci je tah dovoleny
    presuvany_disk = int(z_veza[-1])
    na_disk = int(veze[na][-1] if len(veze[na]) > 0 else MAX_DISK)
    if na_disk < presuvany_disk:
        print("Presunut sa da iba na VACSI disk.")
        return stav_vezi

    # presun disku
    veze[z] = veze[z][:-1]
    veze[na] += str(presuvany_disk)
    vysledny_stav_vezi = "-".join(veze)
    return vysledny_stav_vezi


def nacitaj_tah(poradove_cislo):
    z, na = -1, -1
    while z == -1:
        zna = input(f"{poradove_cislo}. > ")
        if len(zna) == 2 and zna[0].isdigit() and zna[1].isdigit():
            nove_z = int(zna[0]) - 1
            nove_na = int(zna[1]) - 1
            if nove_z in range(POCET_VEZI) and nove_na in range(POCET_VEZI):
                (z, na) = (nove_z, nove_na)
        elif zna.lower() in ["koniec", "exit"]:
            z = PRIKAZ_KONIEC
        else:
            print("ups...")
    return (z, na)


def je_vyhra(stav_vezi):
    return stav_vezi[0:2] == "--" or (stav_vezi[0] == "-" and stav_vezi[-1] == "-")


print("\n" + "*" * 32 + "\nHANOJSKA VEZA\n")
n = int(input("Zadaj pocet poschodi (1-8): "))

hra = vytvorVeze(n)
vypisVeze2(hra)

cislo_tahu = 0
while True:
    cislo_tahu += 1
    (z, na) = nacitaj_tah(cislo_tahu)

    if z == PRIKAZ_KONIEC:
        print("Dakujeme za hru ;)")
        break
    else:
        hra = presun(hra, z, na)
        vypisVeze2(hra)

    if je_vyhra(hra):
        print("Vyhral si :D :D :D")
        break

print()
print()