import random
print('1. feladat\nA pénzfeldobás eredménye: %s'%random.choice(('I','F')))
tipp=input('2. feladat\nTippejen! (F/I)= ')
eredmeny=random.choice(('I','F'))
print('A tipp %s, a dobás eredménye %s volt.\nÖn %s.'%(tipp,eredmeny,'eltalálta' if tipp==eredmeny else 'nem találta el'))
osszes=0
with open('kiserlet.txt') as f:
    for line in f:
        osszes+=1
print('3. feladat\nA kísérlet %d dobásból állt.'%osszes)
fej=0
with open('kiserlet.txt') as f:
    for line in f:
        if line.strip()=='F':
            fej+=1
print('4. feladat\nA kísérlet során a fej relatív gyakorisága %.2lf%% volt.'%(fej/osszes*100))
streak=0
jok=0
maxstreak=0
sor,kezdo,maxkezdo=0,0,0
with open('kiserlet.txt') as f:
    for line in f:
        sor+=1
        if line.strip()=='F':
            if streak==0:
                kezdo=sor
            streak+=1
        else:
            if streak==2:
                jok+=1
            if streak>maxstreak:
                maxstreak=streak
                maxkezdo=kezdo
            streak=0
if streak==2:
    jok+=1
if streak>maxstreak:
    maxstreak=streak
    maxkezdo=kezdo
print('5. feladat\nA kísérlet során %d alkalommal dobtak pontosan két fejet egymás után.'%jok)
print('6. feladat\nA leghosszabb tisztafej sorozat %d tagból áll, kezdete a(z) %d. dobás.'%(maxstreak,maxkezdo))
with open('dobasok.txt','w') as f:
    sorozatok=[''.join(random.choice(('I','F')) for g in range(4)) for i in range(1000)]
    f.write('FFFF: %d, FFFI: %d\n'%(sorozatok.count('FFFF'),sorozatok.count('FFFI')))
    f.write(' '.join(sorozatok))
