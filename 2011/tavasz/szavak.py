def hany_mgh(szo):
    count=0
    for betu in szo:
        if betu in ('a','e','i','o','u'):
            count+=1
    return count
print('1. feladat:')
szo=input('Adj meg egy szót:')
print('Van benne magánhangzó.' if hany_mgh(szo)>0 else 'Nincs benne magánhangzó.')
print('2. feladat:')
leghosszabb=''
with open('szoveg.txt') as f:
    for line in f:
        if len(line.strip())>len(leghosszabb):
            leghosszabb=line.strip()
print('A leghosszabb szó: %s.'%leghosszabb)
print('3. feladat:')
sok_mgh_count=0
ossz_count=0
with open('szoveg.txt') as f:
    for line in f:
        ossz_count+=1
        if len(line.strip())/2<hany_mgh(line.strip()):
            print(line.strip(),end=' ')
            sok_mgh_count+=1
print('%d/%d : %.2f%%'%(sok_mgh_count,ossz_count,sok_mgh_count/ossz_count*100))
print('4. feladat:')
otbetusek=list()
with open('szoveg.txt') as f:
    for line in f:
        if len(line.strip())==5:
            otbetusek.append(line.strip())
harombetu=input('Adj meg három betűt a "létraépítéshez":')
print(' '.join(otbetus for otbetus in otbetusek if otbetus[1:4]==harombetu))
#5. feladat:
letrak=dict()
for otbetus in otbetusek:
    if otbetus[1:4] in letrak:
        letrak[otbetus[1:4]].append(otbetus)
    else:
        letrak[otbetus[1:4]]=[otbetus]
with open('letra.txt','w') as f:
    for letrafok in letrak:
        if len(letrak[letrafok])>1:
            for letraszo in letrak[letrafok]:
                f.write(letraszo+'\n')
            f.write('\n')
##otbetusek.sort(key=lambda elem:elem[1:4])
##with open('letra.txt','w') as f:
##    akt_fok=None
##    if otbetusek[0][1:4]==otbetusek[1][1:4]:
##        f.write('%s\n'%otbetusek[0])
##        akt_fok=otbetusek[0][1:4]
##    for i in range(1,len(otbetusek)):
##        if otbetusek[i][1:4]==akt_fok:
##            f.write('%s\n'%otbetusek[i])
##        elif i+1<len(otbetusek) and otbetusek[i+1][1:4]==otbetusek[i][1:4]:
##            if akt_fok!=None:
##                f.write('\n')
##            f.write('%s\n'%otbetusek[i])
##            akt_fok=otbetusek[i][1:4]