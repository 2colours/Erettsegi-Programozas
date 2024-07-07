class Esemeny:
    def __init__(self, adatsor):
        reszek = adatsor.split(' ')
        self.azonosito = reszek[0]
        self.ora, self.perc = map(int, reszek[1].split(':'))
        self.esemeny = int(reszek[2]) # 1 - belépett, 2 - kilépett, 3 - ebédelt, 4 - könyvet kölcsönzött

#1. feladat
with open('bedat.txt') as f:
    esemenyek = [Esemeny(sor.strip()) for sor in f]
print('2. feladat')
print('Az első tanuló %02d:%02d-kor lépett be a főkapun.'%(esemenyek[0].ora, esemenyek[0].perc))
print('Az utolsó tanuló %02d:%02d-kor lépett ki a főkapun.'%(esemenyek[-1].ora, esemenyek[-1].perc))
#3. feladat
with open('kesok.txt', 'w') as f:
    for esemeny in esemenyek:
        if (esemeny.ora, esemeny.perc) > (8, 15): # innentől mind túl nagy -> nem késés
            break

        if (esemeny.ora, esemeny.perc) <= (7, 50): # még túl kicsi -> nem késés, megyünk tovább
            continue

        f.write('%d:%d %s\n'%(esemeny.ora, esemeny.perc, esemeny.azonosito))
print('4. feladat')
ebedelok_szama = 0
for esemeny in esemenyek:
    if esemeny.esemeny == 3:
        ebedelok_szama += 1
print('A menzán aznap %d tanuló ebédelt.'%ebedelok_szama)
print('5. feladat')
ma_kolcsonzott = set()
kolcsonzok_szama = 0
for esemeny in esemenyek:
    if esemeny.esemeny == 4:
        if esemeny.azonosito not in ma_kolcsonzott:
            kolcsonzok_szama += 1
            ma_kolcsonzott.add(esemeny.azonosito)
print('Aznap %d tanuló kölcsönzött a könyvtárban.'%kolcsonzok_szama)
print('Nem voltak többen, mint a menzán.' if kolcsonzok_szama <= ebedelok_szama else 'Többen voltak, mint a menzűn.')
print('6. feladat')
erintett_tanulok = []
utoljara_ki_vagy_be = dict() # azonosító szerint: utoljára kiment vagy bejött?
for esemeny in esemenyek:
    if (esemeny.ora, esemeny.perc) >= (11, 0): # becsöngetnek - ami innentől kezdve történik, számunkra nem érdekes
        break

    if esemeny.esemeny not in [1, 2]: # csak a kijövetel és bemenetel érdekes
        continue

    # nagyon szigorú logika: azokat nem veszi figyelembe, akik belógtak az óra után majd egyből ki
    if (esemeny.ora, esemeny.perc) <= (10, 50) and esemeny.esemeny == 2:
        utoljara_ki_vagy_be[esemeny.azonosito] = 2 # monoton növekvés miatt az utolsó esemény fog végül érvényre jutni
    if (esemeny.ora, esemeny.perc) < (10, 45) and esemeny.esemeny == 1:
        utoljara_ki_vagy_be[esemeny.azonosito] = 1 # monoton növekvés miatt az utolsó esemény fog végül érvényre jutni
    
    if (esemeny.ora, esemeny.perc) > (10, 50) and esemeny.esemeny == 1: # 10:50 után bejött: lássuk, bent volt-e 10:45-ig!
        try:
            if utoljara_ki_vagy_be[esemeny.azonosito] == 1:
                erintett_tanulok.append(esemeny.azonosito)
        except KeyError: # frissen érkezett: nem baj
            pass
print('Az érintett tanulók:')
print(' '.join(erintett_tanulok))
print('7. feladat')
azonosito = input('Egy tanuló azonosítója=')
bejott = (7, 0)
lattuk_bejonni = False
kiment = (19, 0)
for esemeny in esemenyek:
    if esemeny.azonosito != azonosito:
        continue

    if esemeny.esemeny == 1 and not lattuk_bejonni:
        lattuk_bejonni = True
        bejott = (esemeny.ora, esemeny.perc)
    
    if esemeny.esemeny == 2:
        kiment = (esemeny.ora, esemeny.perc)
kulonbseg_percben = (kiment[0]*60+kiment[1]) - (bejott[0]*60+bejott[1])
print('A tanuló érkezése és távozása között %d óra %d perc telt el.'%(kulonbseg_percben // 60, kulonbseg_percben % 60))
