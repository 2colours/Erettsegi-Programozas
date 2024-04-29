class Valtozas:
    def __init__(self,adatsor):
        adatok=adatsor.split(' ')
        self.ora=int(adatok[0])
        self.perc=int(adatok[1])
        self.szemely=int(adatok[2])
        self.irany=adatok[3]
    def minusz_perc(self,other):
        return self.ora*60+self.perc-other.ora*60-other.perc
#1. feladat
data=list()
with open('ajto.txt') as f:
    for line in f:
        data.append(Valtozas(line.strip()))
print('2. feladat:')
for valt in data:
    if valt.irany=='be':
        print('Először belépett: %s.'%valt.szemely)
        break
for valt in reversed(data):
    if valt.irany=='ki':
        print('Utoljára távozott: %s.'%valt.szemely)
        break
#3. feladat
athaladasok=dict()
for valt in data:
    if valt.szemely not in athaladasok:
        athaladasok[valt.szemely]=1
    else:
        athaladasok[valt.szemely]+=1
with open('athaladas.txt','w') as f:
    for szemely,ath_szam in sorted(athaladasok.items()):
        f.write('%d %d\n'%(szemely,ath_szam))
print('4. feladat:')
vegallapot=dict()
for valt in data:
    vegallapot[valt.szemely]=valt.irany
print('A végén a társalgóban voltak: %s.'%' '.join(str(szemely) for szemely,v_all in vegallapot.items() if v_all=='be'))
print('5. feladat:')
most_bent=0
for valt in data:
    most_bent+=1 if valt.irany=='be' else -1
    valt.ezutan_bent=most_bent
max_letszam_valtozasa=max(data,key=lambda valt:valt.ezutan_bent)
print('Például %d:%d-kor voltak a legtöbben a társalgóban.'%(max_letszam_valtozasa.ora,max_letszam_valtozasa.perc))
print('6. feladat:')
azon=int(input('Kérek egy felhasználó-azonosítót: '))
print('7. feladat:')
utoljara_be=None
osszesen_bent=0
for valt in data:
    if valt.szemely!=azon:
        continue
    print('%d:%d%s'%(valt.ora,valt.perc,'-' if valt.irany=='be' else '\n'),end='')
    if valt.irany=='be':
        utoljara_be=valt
    else:
        osszesen_bent+=valt.minusz_perc(utoljara_be)
print('\n8. feladat:')
if vegallapot[azon]=='be':
    osszesen_bent+=Valtozas('15 0 %d ki'%azon).minusz_perc(utoljara_be)
print('A(z) %d. személy %d percet tartózkodott bent, a megfigyelés végén %s.'%(azon,osszesen_bent,'is ott volt' if vegallapot[azon]=='be' else 'már kint volt'))
