#1. feladat
with open('penztar.txt') as f:
    data=f.read().split('\nF\n')
del data[len(data)-1]
for i in range(len(data)):
    data[i]=data[i].split('\n')
print('2. feladat:\n%d fizetés történt.'%len(data))
print('3. feladat:\n%d árucikk volt az első vásárló kosarában.'%len(data[0]))
print('4. feladat:')
vszam=int(input('Adja meg egy vásárló sorszámát!'))
arunev=input('Adja meg egy árucikk nevét!')
dbszam=int(input('Adja meg a vásárolt darabszámot!'))
print('5. feladat:')
for i in range(len(data)):
    if arunev in data[i]:
        print('%s-t először a(z) %d. vásárláskor vettek.'%(arunev,i+1))
        break
for i in range(len(data)-1,-1,-1):
    if arunev in data[i]:
        print('%s-t utoljára a(z) %d. vásárláskor vettek.'%(arunev,i+1))
        break
print('A %s árucikkből %d vásárláskor vettek.'%(arunev,sum(1 for elem in data if arunev in elem)))
print('6. feladat:')
def ertek(db):
    return 500*db-(100*(db-2) if db>=3 else 0)-(50 if db>=2 else 0)
print('%d darab vételekor fizetendő: %d Ft.'%(dbszam,ertek(dbszam)))
print('7. feladat:')
kiirt=set()
for elem in data[vszam-1]:
    if elem in kiirt:
        continue
    print('%d %s'%(data[vszam-1].count(elem),elem))
    kiirt.add(elem)
#8. feladat
with open('osszeg.txt','w') as f:
    for i in range(len(data)):
        osszeg=0
        szamolt=set()
        for elem in data[i]:
            if elem in szamolt:
                continue
            osszeg+=ertek(data[i].count(elem))
            szamolt.add(elem)
        f.write('%d: %d\n'%(i+1,osszeg))
