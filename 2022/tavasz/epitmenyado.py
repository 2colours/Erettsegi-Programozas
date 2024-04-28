class Telekadat:
      def __init__(self, sor):
          sor_elemek = sor.split(' ')
          self.adoszam, self.utcanev, self.hazszam, self.adosav = sor_elemek[:4]
          self.alapterulet = int(sor_elemek[4])

      def cim(self):
          return '%s utca %s'%(self.utcanev, self.hazszam)

      def ado(self):
          return ado(self.adosav, self.alapterulet)



#1. feladat
adosavok = []
telekadatok = []
with open('utca.txt') as f:
     adosavok = [int(elem) for elem in f.readline().strip().split(' ')]
     for line in f:
         telekadatok.append(Telekadat(line.strip()))
print('2. feladat. A mintában %d telek szerepel.'%len(telekadatok))
print('3. feladat.', end='')
adoszam_be = input('Egy tulajdonos adószáma: ')
votma = False
for adat in telekadatok:
    if adat.adoszam == adoszam_be:
       print(adat.cim())
       votma = True
if not votma:
   print('Nem szerepel az adatállományban.')
'''
for cime in map(Telekadat.cim, filter(lambda ta: ta.adoszam == adoszam_be, telekadatok)):
    print(cime)
'''
#4. feladat
def ado(adosav, alapterulet):
    adosav_index = ord(adosav) - ord('A')
    keplet = adosavok[adosav_index] * alapterulet
    return 0 if keplet < 10000 else keplet
print('5. feladat')
ado_telek_savonkent = dict()
for adat in telekadatok:
    if adat.adosav in ado_telek_savonkent:
       ado_telek_savonkent[adat.adosav][0] += adat.ado()
       ado_telek_savonkent[adat.adosav][1] += 1
    else:
         ado_telek_savonkent[adat.adosav] = [adat.ado(), 1]
'''for adosav, (ado_osszeg, telekszam) in sorted(ado_telek_savonkent.items(), key=lambda pair: pair[0]):
    print('%s sávba %d telek esik, az adó %d Ft.'%(adosav, telekszam, ado_osszeg))'''
for adosav in ('A', 'B', 'C'):
    print('%s sávba %d telek esik, az adó %d Ft.'%(adosav, ado_telek_savonkent[adosav][1], ado_telek_savonkent[adosav][0]))
print('6. feladat. A több sávba sorolt utcák:')
elozo_utca, elozo_adosav = None, None
tobbsavosak = set()
for adat in telekadatok:
    if elozo_utca == adat.utcanev and elozo_adosav != adat.adosav:
       tobbsavosak.add(adat.utcanev)
    elozo_utca = adat.utcanev
    elozo_adosav = adat.adosav
print('\n'.join(sorted(tobbsavosak)))
#7. feladat
tulaj_ado = dict()
for adat in telekadatok:
    if adat.adoszam in tulaj_ado:
       tulaj_ado[adat.adoszam] += adat.ado()
    else:
         tulaj_ado[adat.adoszam] = adat.ado()
with open('fizetendo.txt', 'w') as f:
     f.write('\n'.join('%s %s'%item for item in tulaj_ado.items()))