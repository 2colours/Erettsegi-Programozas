#1. feladat
data=list()
with open('valaszok.txt') as f:
    megoldasok=f.readline().strip()
    for line in f:
        data.append(line.rstrip().split(' '))
print('2. feladat:\n%d résztvevő volt.'%len(data))
print('3. feladat:')
azon=input('A versenyző azonosítója = ')
for i in range(len(data)):
    if data[i][0]==azon:
        sorszama=i
        break
print('%s (a versenyző válasza)'%data[sorszama][1])
print('4. feladat:')
print('%s (a helyes megoldás)'%megoldasok)
helyes=''.join('+' if megoldasok[i]==data[sorszama][1][i] else ' ' for i in range(14))
print('%s (a versenyző helyes válaszai)'%helyes)
print('5. feladat:')
f_index=int(input('A feladat sorszáma = '))-1
counter=0
for sor in data:
    if sor[1][f_index]==megoldasok[f_index]:
        counter+=1
print('A feladatra %d fő, a versenyzők %f%%-a adott helyes választ.'%(counter,100*counter/len(data)))
#6. feladat
def pontoz(proba):
    pontszam=0
    for i in range(14):
        if proba[i]==megoldasok[i]:
            pontszam+=3 if i<5 else 4 if i<10 else 5 if i<13 else 6
    return pontszam
with open('pontok.txt','w') as f:
    for sor in data:
        f.write('%s %d\n'%(sor[0],pontoz(sor[1])))
print('7. feladat:')
data.sort(key=lambda sor:pontoz(sor[1]))
data.reverse()
elozo_pont=pontoz(data[0][1])
print('1. díj (%d pont): %s'%(elozo_pont,data[0][0]))
helyezes=1
for i in range(1,len(data)):
    if pontoz(data[i][1])<elozo_pont:
        helyezes+=1
        elozo_pont=pontoz(data[i][1])
    if helyezes<=3:
        print('%d. díj (%d pont): %s'%(helyezes,elozo_pont,data[i][0]))
    else:
        break
