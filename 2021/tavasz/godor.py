print('1. feladat')
melysegek = list()
with open('melyseg.txt') as f:
     for line in f:
         melysegek.append(int(line.strip()))
print('A fájl adatainak száma: %d'%len(melysegek))


print('2. feladat')
tav = int(input('Adjon meg egy távolságértéket!'))
print('Ezen a helyen a felszín %d méter mélyen van.'%melysegek[tav-1])

print('3. feladat')
print('Az érintetlen terület aránya %.2f%%. '%(sum(map(lambda melyseg: 1 if melyseg == 0 else 0, melysegek))/len(melysegek)*100))

#4. feladat
with open('godrok.txt', 'w') as f:
  i = 0
  godrok = 0 #hány gödör volt eddig
  while True:
        while i < len(melysegek) and melysegek[i] == 0:
              i += 1
        if i == len(melysegek):
           break
        if godrok > 0:
           f.write('\n')
        godrok += 1
        f.write('%d'%melysegek[i])
        i += 1
        while melysegek[i] != 0:
              f.write(' %d'%melysegek[i])
              i += 1


print('5. feladat')
print('A gödrök száma: %d'%godrok)

print('6. feladat')
if melysegek[tav-1] == 0:
   print('Az adott helyen nincs gödör.')
   exit(0)
print('a)')
eleje, vege = tav, tav
while melysegek[eleje-2] != 0:
      eleje -= 1
while melysegek[vege] != 0:
      vege += 1
print('A gödör kezdete: %d méter, a gödör vége: %d méter.'%(eleje, vege))
print('b)')
tulvagyunk = False #túlvagyunk-e a lokális maximumon
for i in range(eleje-1, vege-1):
    if melysegek[i] < melysegek[i+1] and tulvagyunk:
       print('Nem mélyül folyamatosan.')
       break
    if melysegek[i] > melysegek[i+1]:
       tulvagyunk = True
else:
     print('Folyamatosan mélyül.')
print('c)')
print('A legnagyobb mélysége %d méter.'%max(melysegek[eleje-1:vege]))
print('d)')
print('A térfogata %d m^3.'%(sum(melysegek[eleje-1:vege])*10))
print('e)')
print('A vízmennyiség %d m^3.'%((sum(melysegek[eleje-1:vege]) - (vege - eleje + 1))*10))