print('1. feladat: szöveg hossza')
s = input('Szöveg: ')
szam = int(input('Szám : '))
if len(s) == szam:
    print('A szöveg hossza egyenlő a számmal')
elif len(s) > szam:
    print('A szöveg hossza nagyobb a számnál')
else:
    print('A szöveg hossza kisebb a számnál')
