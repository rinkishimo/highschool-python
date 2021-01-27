def over_rc(rc):
    rc2 = ""
    for z in rc.strip():
        if z.isdigit():
            rc2 += z

    # 10 znakov
    if len(rc2) != 10:
        return False, "nespravny pocet cislic"

    # 3,4 pozicia - 01-12 / 51-62
    mesiac = int(rc2[2:4])
    if not (1 <= mesiac <= 12 or 51 <= mesiac <= 62):
        return False, "nespravny mesiac"

    # delitelnost 11
    if int(rc2) % 11 != 0:
        return False, "nedelitelne 11"

    return True, "ok"


print()
print(
    "Vitajte, zadajte rodne cislo pre overenie alebo prazdny retazec pre ukoncenie programu."
)
while True:
    rodne_cislo = input("- rodne cislo: ")
    if rodne_cislo.strip() == "":
        break

    stav, sprava = over_rc(rodne_cislo)
    if stav == True:
        print("- rodne cislo je ok")
    else:
        print(f"- toto nie je rodne cislo ({sprava})")

print("Dovidenia")
print()
