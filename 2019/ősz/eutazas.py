class Felszallas:
    def __init__(self,line):
        elements=line.split(' ')
        self.ssz=int(elements[0])
        felsz_elements=elements[1].split('-')
        self.felsz_datum=felsz_elements[0] #szövegként
        self.felsz_ido=felsz_elements[1]
        self.azon=elements[2]
        self.tipus=elements[3]
        self.erv_data=elements[4] #szövegként

    def ervenyes(self):
        return self.tipus=='JGY' and self.erv_data!='0'\
            or self.tipus!='JGY' and self.felsz_datum<=self.erv_data

    def kedvezmenyes(self):
        return self.tipus in ('TAB','NYB')

    def ingyenes(self):
        return self.tipus in ('NYP','RVS','GYK')

    def hamar_lejar(self):
        return self.tipus!='JGY' and self.ervenyes() and napokszama(*datum_szetbont(self.felsz_datum),*datum_szetbont(self.erv_data))<=3

#1. feladat:
data=list()
with open('utasadat.txt') as f:
    for line in f:
        data.append(Felszallas(line.strip()))
print('2. feladat\nA buszra %d utas akart felszállni.'%len(data))
print('3. feladat')
'''
ervenytelen_count=0
for felsz in data:
    if not felsz.ervenyes():
        ervenytelen_count+=1
'''
ervenytelen_count=sum(1 for felsz in data if not felsz.ervenyes())
print('A buszra %d utas nem szállhatott fel.'%ervenytelen_count)
print('4. feladat')
megallonkent_count=dict()
for felsz in data:
    ssz=felsz.ssz
    if ssz not in megallonkent_count:
        megallonkent_count[ssz]=0
    megallonkent_count[ssz]+=1
legzsufoltabb_item=max(megallonkent_count.items(),key=lambda item:(item[1],-item[0]))
print('A legtöbb utas (%d fő) a %d. megállóban próbált felszállni.'%(legzsufoltabb_item[1],legzsufoltabb_item[0]))
print('5. feladat')
kedv_count=ingy_count=0
ervenyes_data=filter(Felszallas.ervenyes,data)
for felsz in ervenyes_data:
    if felsz.kedvezmenyes():
        kedv_count+=1
    elif felsz.ingyenes():
        ingy_count+=1
print('''Ingyenesen utazók száma: %d fő
A kedvezményesen utazók száma: %d fő'''%(ingy_count,kedv_count))

#6. feladat:
def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1

def datum_szetbont_str(datum):
    return (datum[:4],datum[4:6],datum[6:])

def datum_szetbont(datum):
    return tuple(int(elem) for elem in datum_szetbont_str(datum))

def kotojeles_format(datum):
    return '-'.join(datum_szetbont_str(datum))


with open('figyelmeztetes.txt','w') as f:
    f.write('\n'.join('%s %s'%(felsz.azon,kotojeles_format(felsz.erv_data)) for felsz in data if felsz.hamar_lejar()))
