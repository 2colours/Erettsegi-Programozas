#1. feladat
def mpbe(o,p,mp):
    return o*3600+p*60+mp

#2. feladat
data=list()
with open('hivas.txt') as f:
    for line in f:
        data.append([int(elem) for elem in line.strip().split(' ')])
print('3. feladat:')
orankent=[0]*24
for elem in data:
    orankent[elem[0]]+=1
for i in range(24):
    if orankent[i]>0:
        print('%d óra %d hívás'%(i,orankent[i]))
print('4. feladat:')
def idotartam(x):
    return mpbe(x[3],x[4],x[5])-mpbe(x[0],x[1],x[2])
maxsor=max(data,key=idotartam)
print('A leghosszabb ideig vonalban levő hívó a(z) %d. sorban szerepel, a hívás hossza: %d másodperc.'%(data.index(maxsor)+1,idotartam(maxsor)))
print('5. feladat:')
idopont=[int(elem) for elem in input('Adjon meg egy időpontot! (óra perc másodperc)').split(' ')]
hanyan=-1
ki_beszel=-1
for i in range(len(data)):
    #if mpbe(data[i][0],data[i][1],data[i][2])<=mpbe(idopont[0],idopont[1],idopont[2]) and mpbe(idopont[0],idopont[1],idopont[2])<mpbe(data[i][3],data[i][4],data[i][5]):
    if tuple(data[i][:3])<=tuple(idopont)<tuple(data[i][3:]):
        hanyan+=1
        if hanyan==0:
            ki_beszel=i
print('Nem volt beszélő.' if ki_beszel==-1 else 'A várakozók száma: %d a beszélő a %d. hívó.'%(hanyan,ki_beszel+1))
print('6. feladat:')
def sikeres(sor,eddigmax):
    return sor[0]<12 and (sor[3],sor[4],sor[5])>eddigmax
eddigmax=(8,0,0)
with open('sikeres.txt','w') as f:
    for i in range(len(data)):
        if sikeres(data[i],eddigmax):
            utso=(i,eddigmax[0],eddigmax[1],eddigmax[2])
            f.write('%d %d %d %d %d %d %d\n'%(i+1,eddigmax[0],eddigmax[1],eddigmax[2],data[i][3],data[i][4],data[i][5]))
            eddigmax=tuple(data[i][3:])
vart=mpbe(utso[1],utso[2],utso[3])-mpbe(data[utso[0]][0],data[utso[0]][1],data[utso[0]][2])
print('Az utolsó telefonáló adatai a(z) %d. sorban vannak, %d másodpercig várt.'%(utso[0]+1,vart))
