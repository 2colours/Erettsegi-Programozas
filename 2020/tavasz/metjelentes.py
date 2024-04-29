class Adat:
    def __init__(self,line):
        szeletek=line.split(' ')
        self.telepules=szeletek[0]
        self.ido=(int(szeletek[1][:2],base=10),int(szeletek[1][2:],base=10))
        self.szel=szeletek[2]
        self.homerseklet=int(szeletek[3],base=10)

class Statisztika:
    def __init__(self):
        self.hom_osszeg=0
        self.orak=set()
        self.darab=0

        self.hom_min=None
        self.hom_max=None

    def frissit_kh(self,homerseklet,ora):
        self.hom_osszeg+=homerseklet
        self.darab+=1
        self.orak.add(ora)

    def frissit_hoingas(self,homerseklet):
        if self.hom_min==None or self.hom_min>homerseklet:
            self.hom_min=homerseklet
        if self.hom_max==None or self.hom_max<homerseklet:
            self.hom_max=homerseklet

    def hoingas(self):
        return self.hom_max-self.hom_min

    def hom_atlag(self):
        return self.hom_osszeg/self.darab
#1. feladat
adatok=list()
with open('tavirathu13.txt') as f:
    for line in f:
        adatok.append(Adat(line.strip()))
print('2. feladat')
be_telepules=input('Adja meg egy település kódját! Település: ')
utolso_idopont=max(elem.ido for elem in adatok if elem.telepules==be_telepules)
print('Az utolsó mérési adat a megadott településről %d:%d-kor érkezett.'%utolso_idopont)
print('3. feladat')
kishom_adat=min(adatok,key=lambda elem:elem.homerseklet)
nagyhom_adat=max(adatok,key=lambda elem:elem.homerseklet)
print('A legalacsonyabb hőmérséklet: %s %02d:%02d %d fok.'%(kishom_adat.telepules,*kishom_adat.ido,kishom_adat.homerseklet))
print('A legmagasabb hőmérséklet: %s %02d:%02d %d fok.'%(nagyhom_adat.telepules,*nagyhom_adat.ido,nagyhom_adat.homerseklet))
print('4. feladat')
volt_szelcsend=False
for elem in adatok:
    if elem.szel=='00000':
        volt_szelcsend=True
        print('%s %02d:%02d'%(elem.telepules,*elem.ido))
if not volt_szelcsend:
    print('Nem volt szélcsend a mérések idején.')
'''
szelcsend_sorok=['%s %02d:%02d'%(elem.telepules,*elem.ido) for elem in adatok if elem.szel=='00000']
if len(szelcsend_sorok)==0:
    print('Nem volt szélcsend a mérések idején.')
else:
    print('\n'.join(szelcsend_sorok))'''
print('5. feladat')
statisztikak=dict()
for elem in adatok:
    if elem.telepules not in statisztikak:
        statisztikak[elem.telepules]=Statisztika()
    statisztikak[elem.telepules].frissit_hoingas(elem.homerseklet)
    if elem.ido[0] in (1,7,13,19):
        statisztikak[elem.telepules].frissit_kh(elem.homerseklet,elem.ido[0])
for (telepules,statisztika) in statisztikak.items():
    print(telepules,end=' ')
    if len(statisztika.orak)!=4:
        print('NA',end=' ')
    else:
        print('Középhőmérséklet: %d;'%round(statisztika.hom_atlag()),end=' ')
    print('Hőmérséklet-ingadozás: %d'%statisztika.hoingas())
#6. feladat
sorok_kiirni=dict()
for elem in adatok:
    if elem.telepules not in sorok_kiirni:
        sorok_kiirni[elem.telepules]=list()
    sorok_kiirni[elem.telepules].append('%02d:%02d %s'%(*elem.ido,'#'*int(elem.szel[3:])))
for (telepules,tsorok) in sorok_kiirni.items():
    with open('%s.txt'%telepules,'w') as f:
        f.write('%s\n'%telepules)
        f.write('\n'.join(tsorok))
