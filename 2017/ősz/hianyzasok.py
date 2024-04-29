class Nap:
    def __init__(self,honap,nap):
        self.honap=honap
        self.nap=nap
        self.diakok=list()
    def uj_diak(self,diak):
        self.diakok.append(diak)
class Diak:
    def __init__(self,vnev,knev,jelenlet):
        self.vnev=vnev
        self.knev=knev
        self.jelenlet=jelenlet
def hetnapja(honap,nap):
    napnev=['vasárnap','hétfő','kedd','szerda','csütörtök',\
            'péntek','szombat']
    napszam=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam=(napszam[honap-1]+nap)%7
    return napnev[napsorszam]
    '''
honap
nap
diakok: tömb, elemei: vnev,knev,jelenlet
'''
napok=list()
with open('naplo.txt') as f:
    for sor in f:
        sor=sor.strip().split(' ')
        if sor[0]=='#':
            napok.append(Nap(int(sor[1]),int(sor[2])))
        else:
            napok[len(napok)-1].uj_diak(Diak(sor[0],sor[1],sor[2]))
print('2. feladat:\n%d sor rögzít hiányzást.'%sum(len(nap.diakok) for nap in napok))
print('3. feladat:')
print('Igazolt hiányzások: %d óra.'%sum(diak.jelenlet.count('X') for nap in napok for diak in nap.diakok))
print('Igazolatlan hiányzások: %d óra.'%sum(diak.jelenlet.count('I') for nap in napok for diak in nap.diakok))
print('5. feladat:')
honap=int(input('A hónap sorszáma='))
nap=int(input('A nap sorszáma='))
print('Azon a napon %s volt.'%hetnapja(honap,nap))
print('6. feladat:')
napnev=input('A nap neve=')
ora_ssz=int(input('Az óra sorszáma='))-1
hianyzasok=0
for nap in napok:
    if hetnapja(nap.honap,nap.nap)!=napnev:
        continue
    for diak in nap.diakok:
        if diak.jelenlet[ora_ssz] in ('I','X'):
            hianyzasok+=1
print('Ekkor összesen %d óra hiányzás történt.'%hianyzasok)
print('7. feladat:\nA legtöbbet hiányzó tanulók: ')
hany_orat_logott=dict()
for nap in napok:
    for diak in nap.diakok:
        akt_logas=diak.jelenlet.count('X')+diak.jelenlet.count('I')
        if diak.vnev+' '+diak.knev in hany_orat_logott:
            hany_orat_logott[diak.vnev+' '+diak.knev]+=akt_logas
        else:
            hany_orat_logott[diak.vnev+' '+diak.knev]=akt_logas
max_logas=max(hany_orat_logott.values())
for nev,logas in hany_orat_logott.items():
    if logas==max_logas:
        print(nev,end=' ')
