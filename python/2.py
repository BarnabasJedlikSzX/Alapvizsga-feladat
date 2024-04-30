import random

def atlag(mylist):
    return sum(mylist) / len(mylist)

print('2. feladat: Átlag:')
for i in range(5):
    mylist = [random.randint(1, 100) for _ in range(4)]
    print(f'  {i+1}: {mylist} -> {atlag(mylist)}')

