#!/usr/bin/env python3


#1. feladat
with open('osvenyek.txt') as f:
    osvenyek = [list(sor.strip()) for sor in f]

with open('dobasok.txt') as f:
    dobasok = [int(elem) for elem in f.readline().strip().split(' ')]

print('2. feladat')
print('A dobások száma: %d'%len(dobasok))
print('Az ösvények száma: %d'%len(osvenyek))

print('3. feladat')
leghosszabb_index, leghosszabb_ertek = max(map(lambda par: (par[0] + 1, len(par[1])), enumerate(osvenyek)), key=lambda par: par[1])
print('Az egyik leghosszabb a(z) %d. ösvény, hossza: %d'%(leghosszabb_index, leghosszabb_ertek))

print('4. feladat')
valasztott_osveny = int(input('Adja meg egy ösvény sorszámát!'))
valasztott_jatekos_szam = int(input('Adja meg a játékosok számát!'))

print('5. feladat')
# a) beépített Counter dict
'''
from collections import Counter
valasztott_osveny_mezok = Counter(osvenyek[valasztott_osveny-1])
for mezo_tipus, darabszam in valasztott_osveny_mezok.items():
    print('%c: %d darab'%(mezo_tipus, darabszam))
    '''
# b) manuális "counter" dict
'''
valasztott_osveny_mezok = dict()
for mezo in osvenyek[valasztott_osveny-1]:
    if mezo not in valasztott_osveny_mezok:
        valasztott_osveny_mezok[mezo] = 1
    else:
        valasztott_osveny_mezok[mezo] += 1
for mezo_tipus, darabszam in valasztott_osveny_mezok.items():
    print('%c: %d darab'%(mezo_tipus, darabszam))
    '''
# c) count használata (okosan)
for mezo_tipus in ('M', 'V', 'E'):
    darab = osvenyek[valasztott_osveny-1].count(mezo_tipus)
    if darab > 0:
        print('%c: %d darab'%(mezo_tipus, darab))


#6. feladat
with open('kulonleges.txt', 'w') as f:
    for index, mezo in enumerate(osvenyek[valasztott_osveny-1]):
        if mezo == 'M':
            continue

        f.write('%d\t%c\n'%(index+1, mezo))

print('7. feladat')
valasztott_osveny_hossz = len(osvenyek[valasztott_osveny-1])
jatekos_poziciok = [0] * valasztott_jatekos_szam
vege = False
dobas_iterator = iter(dobasok)
korszam = 0
while not vege:
    korszam += 1
    for jatekos_index in range(valasztott_jatekos_szam):
        mostani_dobas = next(dobas_iterator)
        jatekos_poziciok[jatekos_index] += mostani_dobas
        if jatekos_poziciok[jatekos_index] >= valasztott_osveny_hossz:
            vege = True
messze_jutott_index = jatekos_poziciok.index(max(jatekos_poziciok))
print('A játék a(z) %d. körben fejeződött be. A legtávolabb jutó(k) sorszáma: %d'%(korszam, messze_jutott_index + 1))

print('8. feladat')
jatekos_poziciok = [0] * valasztott_jatekos_szam
vege = False
dobas_iterator = iter(dobasok)
nyertesek = []
while not vege:
    for jatekos_index in range(valasztott_jatekos_szam):
        mostani_dobas = next(dobas_iterator)
        jatekos_poziciok[jatekos_index] += mostani_dobas
        if jatekos_poziciok[jatekos_index] >= valasztott_osveny_hossz:
            nyertesek.append(str(jatekos_index+1))
            vege = True
            continue
        
        mostani_mezo = osvenyek[valasztott_osveny-1][jatekos_poziciok[jatekos_index]-1]
        if mostani_mezo == 'E':
            jatekos_poziciok[jatekos_index] += mostani_dobas
        elif mostani_mezo == 'V':
            jatekos_poziciok[jatekos_index] -= mostani_dobas

print('Nyertes(ek): %s'%(' '.join(nyertesek)))
print('A többiek pozíciója:')
for index, pozicio in enumerate(jatekos_poziciok):
    if str(index+1) in nyertesek:
        continue

    print('%d. játékos, %d. mező'%(index+1, pozicio))
