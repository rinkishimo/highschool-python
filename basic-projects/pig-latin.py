def sk2piglatin(slovo):
    if slovo[0] in 'aeiouy':
        vysledok = slovo + 'way'
    else:
        vysledok = slovo[1:] + slovo[0] + 'ay'
    return vysledok


veta = input('Zadaj vetu na preklad: ')
slova = veta.split(' ')
prelozeneSlova = []

for slovo in slova:
    plSlovo = sk2piglatin(slovo)
    #print(slovo, '->', plSlovo)
    prelozeneSlova.append(plSlovo)
    #print(prelozeneSlova)

prelozenaVeta = ' '.join(prelozeneSlova)
print(prelozenaVeta)


#print('-'.join(prelozeneSlova))


