import random
import string

def encode(message):
    balast = string.digits + string.ascii_letters
    vysledok = ''
    for pismenko in message:
        vysledok += random.choice(balast) + pismenko + random.choice(balast)
    vysledok = vysledok.replace(' ', '%')
    return vysledok

def decode(message):
    vysledok = message[1::3]
    vysledok = vysledok.replace('%', ' ')
    return vysledok


povodnaSprava = input('Zadaj spravu pre zasifrovanie: ')
zasifrovana = encode(povodnaSprava)
odsifrovana = decode(zasifrovana)

print(f'{zasifrovana} -> {odsifrovana}')