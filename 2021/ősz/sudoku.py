print('1. feladat')
fnev = input('Adja meg a bemeneti fájl nevét!')
ssz = int(input('Adja meg egy sor számát!'))
osz = int(input('Adja meg egy oszlop számát!'))
#2. feladat
with open(fnev) as f:
     tablazat = [list(map(int, f.readline().strip().split(' '))) for i in range(9)]
     tippek = list()
     for line in f:
         tippek.append(tuple(map(int, line.strip().split(' '))))
print('3. feladat')
akt_mezo = tablazat[ssz-1][osz-1]
print('Az adott helyet még nem töltötték ki.' if akt_mezo == 0 else 'Az adott helyen szereplő szám: %d'%akt_mezo)
def mezo0_to_rt0(sor0, oszlop0):
    return (sor0 // 3) * 3 + (oszlop0 // 3)
print('A hely a(z) %d résztáblázathoz tartozik.'%(1+mezo0_to_rt0(ssz-1, osz-1)))
print('4. feladat')
ures_mezok = sum(1 if mezo == 0 else 0 for sor in tablazat for mezo in sor)
print('Az üres helyek aránya: %.1f%%'%(ures_mezok/81*100))
print('5. feladat')
for tipp in tippek:
    tipp_ertek, tipp_ssz, tipp_osz = tipp
    print('A kiválasztott sor: %d oszlop: %d a szám: %d'%(tipp_ssz, tipp_osz, tipp_ertek))
    if tablazat[tipp_ssz-1][tipp_osz-1] != 0:
       print('A helyet már kitöltötték')
       continue
    if tipp_ertek in tablazat[tipp_ssz-1]:
       print('Az adott sorban már szerepel a szám')
       continue
    if tipp_ertek in [tablazat[akt_sor][tipp_osz-1] for akt_sor in range(9)]:
       print('Az adott oszlopban már szerepel a szám')
       continue
    tipp_rt0 = mezo0_to_rt0(tipp_ssz - 1, tipp_osz - 1)
    if tipp_ertek in [tablazat[tipp_rt0 // 3 * 3 + sor_offset][tipp_rt0 % 3 * 3 + oszlop_offset] for sor_offset in range(3) for oszlop_offset in range(3)]:
       print('Az adott résztáblázatban már szerepel a szám')
       continue
    print('A lépés megtehető')