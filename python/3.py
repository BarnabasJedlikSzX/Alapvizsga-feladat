from classes import Csapat

csapatok: list[Csapat] = []

with open('wro.csv', 'r', encoding='UTF-8') as f:
    max_pont = int(f.readline().strip())
    f.readline()
    for sor in f:
        csapatok.append(Csapat(sor))
    
print('3. feladat: Lego verseny')

print(f'3.2. feladat: Nevezett csapatok száma: {len(csapatok)}')

jedlik_db = 0
for i in csapatok:
    if 'jedlik' in i.nev.lower():   
        jedlik_db += 1

print(f'3.3. feladat: Jedlik-es csapatok száma: {jedlik_db} ')

# 4. feladat: összpont osztályfüggvény létrehozása

# print(csapatok[0].osszpont())


csapatok = sorted(csapatok, key = lambda x: (-x.osszpont(), x.osszido()))

legjobb_csapat = csapatok[0]

print(f'3.5. feladat: legjobb csapat: {legjobb_csapat.nev}\n\tA legjobb csapat elődöntős helyszíne: {legjobb_csapat.helyszin}\n\tA legjobb csapat összpontszáma: {legjobb_csapat.osszpont()}')

mydict = {}

for i in csapatok:
    mydict[i.helyszin] = mydict.get(i.helyszin, 0) + 1

print(f'3.6. feladat: Helyszínenkénti versenyzők: ')

for key, value in mydict.items():
    print(f'\t{key}: {value}')

print(f'3.7. feladat: továbbjutó csapatok: csv')

tovabbjuto_csapatok: list[Csapat] = []


for i in mydict.keys():
    mydict[i] = min(int(mydict[i]/2), 3)
    # print(mydict[i], ' ', i)

for i in csapatok:
    if mydict[i.helyszin] and i.osszpont() / (max_pont*2) *100 > 25:
        mydict[i.helyszin] -= 1
        tovabbjuto_csapatok.append(i)


with open('tovabbjuto_csapatok.csv', 'w', encoding='UTF-8') as f:
    f.write(f'Név;Helyszín;osszpont;osszido')
    for i in tovabbjuto_csapatok:
        f.write(f'{i.nev};{i.helyszin};{i.osszpont()};{i.osszido()}\n')