class Telek:
    paros_hazszam=2
    paratlan_hazszam=1
    def __init__(self,oldal,szel,szin):
        self.oldal=oldal
        self.szel=szel
        self.szin=szin
        if oldal==0:
            self.hazszam=Telek.paros_hazszam
            Telek.paros_hazszam+=2
        else:
            self.hazszam=Telek.paratlan_hazszam
            Telek.paratlan_hazszam+=2
    def oldal_str(self):
        return 'páros' if self.oldal==0 else 'páratlan'
data=[]
def keres_hazszam(hsz):
    for telek in data:
        if telek.hazszam==hsz:
            return telek
    return None
#1. feladat:
with open('kerites.txt') as f:
    for line in f:
        oldal,szel,szin=line.strip().split(' ')
        data.append(Telek(int(oldal),int(szel),szin))
print('2. feladat\nAz eladott telkek száma: %d'%len(data))
print('3. feladat')
utolso=data[-1]
print('A %s oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: %d'%(utolso.oldal_str(),utolso.hazszam))
print('4. feladat')
paratlan_oldal=[elem for elem in data if elem.oldal==1]
for index in range(len(paratlan_oldal)):
    if paratlan_oldal[index].szin not in (':','#') and paratlan_oldal[index+1].szin==paratlan_oldal[index].szin:
        print('A szomszédossal egyezik a kerítés színe: %d'%paratlan_oldal[index].hazszam)
        break
print('5. feladat')
hazszam=int(input('Adjon meg egy házszámot! '))
telek=keres_hazszam(hazszam)
elotte,utana=keres_hazszam(hazszam-2),keres_hazszam(hazszam+2)
print('A kerítés színe / állapota: %s'%telek.szin)
osszes_szin=set(chr(i) for i in range(ord('A'),ord('Z')+1))
lehetseges_szin=osszes_szin-{telek.szin}
if elotte!=None:
    lehetseges_szin-={elotte.szin}
if utana!=None:
    lehetseges_szin-={utana.szin}
print('Egy lehetséges festési szín: %s'%(lehetseges_szin.pop()))
with open('utcakep.txt','w') as f:
    for telek in paratlan_oldal:
        f.write(telek.szin*telek.szel)
    f.write('\n')
    for telek in paratlan_oldal:
        str_hazszam=str(telek.hazszam)
        f.write(str_hazszam+' '*(telek.szel-len(str_hazszam)))
