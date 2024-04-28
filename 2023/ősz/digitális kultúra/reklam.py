#!/usr/bin/env python3

#1. feladat
rendelesek = []
with open('rendel.txt') as f:
    for sor in f:
        sor = sor.strip().split(' ')
        rendelesek.append((int(sor[0]), sor[1], int(sor[2])))

print('2. feladat')
print('A rendelések száma: %d'%len(rendelesek))

print('3. feladat')
valasztott_nap = int(input('Kérem, adjon meg egy napot: '))
print('A rendelések száma az adott napon: %d'%sum(map(lambda rendeles: rendeles[0] == valasztott_nap, rendelesek)))

print('4. feladat')
nr_rendeles_nelkuli_napok_szama = 30 - len(set(rendeles[0] for rendeles in rendelesek if rendeles[1] == 'NR'))
if nr_rendeles_nelkuli_napok_szama == 0:
    print('Minden nap volt rendelés a reklámban nem érintett városból')
else:
    print('%d nap nem volt a reklámban nem érintett városból rendelés'%nr_rendeles_nelkuli_napok_szama)

print('5. feladat')
rendeles_darabszamok = map(lambda rendeles: rendeles[2], rendelesek)
max_darabszam = max(rendeles_darabszamok)
for rendeles in rendelesek:
    if rendeles[2] == max_darabszam:
        print('A legnagyobb darabszám: %d, a rendelés napja: %d'%(max_darabszam, rendeles[0]))
        break

#6. feladat
def osszes(varosnev, napszam):
    return sum(rendeles[2] for rendeles in rendelesek if rendeles[0] == napszam and rendeles[1] == varosnev)

print('7. feladat')
rendelesek_21_varosonkent = {varos: osszes(varos, 21) for varos in ('PL', 'TV', 'NR')}
print('A rendelt termékek darabszáma a 21. napon PL: %d TV: %d, NR: %d'%(rendelesek_21_varosonkent['PL'], rendelesek_21_varosonkent['TV'], rendelesek_21_varosonkent['NR']))

print('8. feladat')
def osszes_intervallummal(varosnev, napintervallum):
    return sum(1 for rendeles in rendelesek if rendeles[0] in napintervallum and rendeles[1] == varosnev)
excel_tabla = {varosnev:{intervallum:osszes_intervallummal(varosnev, intervallum) for intervallum in (range(1, 11), range(11, 21), range(21, 31))} for varosnev in ('PL', 'TV', 'NR')}
print('Napok\t1..10\t11..20\t21..30')
for varosnev, varos_sor in excel_tabla.items():
    print(varosnev, end='\t')
    print('\t'.join(map(str, varos_sor.values())))


