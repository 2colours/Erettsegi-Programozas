class SorAdat:
    def __init__(self,sor):
        darabolt=sor.split(' ')
        self.nap=int(darabolt[0])
        self.ido=darabolt[1]
        self.rendszam=darabolt[2]
        self.szemely=int(darabolt[3])
        self.km_ora=int(darabolt[4])
        self.behajt=bool(int(darabolt[5]))

#1. feladat
adatok=list()
with open('autok.txt') as f:
    for sor in f:
        adatok.append(SorAdat(sor.strip()))
print('2. feladat')
'''
for i in range(len(adatok)-1,-1,-1):
    if not adatok[i].behajt:
        print('%d. nap rendszám: %s'%(adatok[i].nap,adatok[i].rendszam))
        break
'''
#2. megoldás
for sor in reversed(adatok):
    if not sor.behajt:
        print('%d. nap rendszám: %s'%(sor.nap,sor.rendszam))
        break
print('3. feladat')
nap=int(input('Nap: '))
print('Forgalom a(z) %d. napon:'%nap)
print('\n'.join(\
map(lambda sor:'%s %s %d %s'%\
(sor.ido,sor.rendszam,sor.szemely,'be' if sor.behajt else 'ki'),\
filter(lambda sor:sor.nap==nap,adatok))))
print('4. feladat')
'''
kint_van=0
for sor in adatok:
    kint_van+=-1 if sor.behajt else 1
print('A hónap végén %d autót nem hoztak vissza.'%kint_van)
'''
#2. megoldás
kint_van=sum(map(lambda sor:-1 if sor.behajt else 1,adatok))
print('A hónap végén %d autót nem hoztak vissza.'%kint_van)
print('5. feladat')
utolso_km_orak=dict()
for behajt_sor in filter(lambda sor:sor.behajt,reversed(adatok)):
    if behajt_sor.rendszam not in utolso_km_orak:
        utolso_km_orak[behajt_sor.rendszam]=behajt_sor.km_ora
elso_km_orak=dict()
for kihajt_sor in filter(lambda sor:not sor.behajt,adatok):
    if kihajt_sor.rendszam not in elso_km_orak:
        elso_km_orak[kihajt_sor.rendszam]=kihajt_sor.km_ora
for rendszam in elso_km_orak:
    print('%s %d km'%(rendszam,utolso_km_orak[rendszam]-elso_km_orak[rendszam]))
print('6. feladat')
egyeni_rekord=dict()
aktualis_kezdet=dict()
for sor in adatok:
    if sor.behajt:
        megtett_km=sor.km_ora-aktualis_kezdet[sor.szemely]
        if sor.szemely not in egyeni_rekord or egyeni_rekord[sor.szemely]<megtett_km:
            egyeni_rekord[sor.szemely]=megtett_km
    else:
        aktualis_kezdet[sor.szemely]=sor.km_ora
max_elem=max(egyeni_rekord.items(),key=lambda elem:elem[1])
print('Leghosszabb út: %d km, személy: %d'%(max_elem[1],max_elem[0]))
print('7. feladat')
rendszam=input('Rendszám: ')
sorok_rendszamhoz=list(filter(lambda sor:sor.rendszam==rendszam,adatok))
with open('%s_menetlevel.txt'%rendszam,'w') as f:
    for i in range(0,len(sorok_rendszamhoz),2):
        paros_sor=sorok_rendszamhoz[i]
        kiir_sor='%d\t%d. %s\t%d km'%(paros_sor.szemely,paros_sor.nap,paros_sor.ido,paros_sor.km_ora)
        if i+1<len(sorok_rendszamhoz):
            paratlan_sor=sorok_rendszamhoz[i+1]
            kiir_sor+='\t%d. %s\t%d km'%(paratlan_sor.nap,paratlan_sor.ido,paratlan_sor.km_ora)
        f.write(kiir_sor+'\n')