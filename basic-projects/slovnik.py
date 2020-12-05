# prekladovy slovnik

def najdi_preklad(subor_slovnika, hladane_sk_slovo):
    slovnik = open(subor_slovnika, 'r')
    hladane_en_slovo = ''
    while True:
        sk = slovnik.readline().strip()
        if '' == sk:
            break
        en = slovnik.readline().strip()
        if '' == en:
            break
        if (hladane_sk_slovo == sk):
            hladane_en_slovo = en
            break
    slovnik.close()
    return hladane_en_slovo

def zaeviduj_novy_preklad(subor_slovnika, nove_sk_slovo):
    print(f'! slovo "{nove_sk_slovo}" sa v slovniku nenaslo, ale mozes ho doplnit.')
    nove_en_slovo = input(f'? zadaj preklad slova "{nove_sk_slovo}" (iba <enter> pre preskocenie doplnenia): ')
    if ('' != nove_en_slovo):
        slovnik = open(subor_slovnika, 'a')
        slovnik.write(f'{nove_sk_slovo}\n{nove_en_slovo}\n')
        slovnik.close()


subor_slovnika = 'slovnik.txt'
print('*** vitajte v prekladovom slovniku ***')
while True:
    sk_slovo = input('? zadaj slovo na preklad (iba <enter> pre ukoncenie): ')
    if ('' == sk_slovo):
        break

    en_slovo = najdi_preklad(subor_slovnika, sk_slovo)
    if ('' == en_slovo):
        zaeviduj_novy_preklad(subor_slovnika, sk_slovo)
    else:
        print('>', en_slovo)
    
print('*** dovidenia ***')
