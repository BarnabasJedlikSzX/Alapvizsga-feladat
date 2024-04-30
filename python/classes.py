class Eredmény:
    def __init__(self, mylist: list[str]) -> None:
        self.elso_kor_pont = int(mylist[0])
        self.elso_kor_ido = int(mylist[1])
        self.masodik_kor_pont = int(mylist[2])
        self.masodik_kor_ido = int(mylist[3])
        self.harmadik_kor_pont = int(mylist[4])
        self.harmadik_kor_ido = int(mylist[5])

class Csapat: 
    def __init__(self, sor: str) -> None:
        data = sor.strip().split(';')
        self.nev = data[0]
        self.helyszin = data[1]
        self.eredmenyek = Eredmény(data[2:])
        
    def osszpont(self):
        mylist: list[int] = [self.eredmenyek.elso_kor_pont, self.eredmenyek.masodik_kor_pont, self.eredmenyek.harmadik_kor_pont]
        mylist.remove(min(mylist))
        # print(mylist)
        return  sum(mylist)
    
    def osszido(self):
        times = []
        if self.osszpont() == self.eredmenyek.elso_kor_pont + self.eredmenyek.masodik_kor_pont:
            times.append(self.eredmenyek.elso_kor_ido + self.eredmenyek.masodik_kor_ido)
        if self.osszpont() == self.eredmenyek.harmadik_kor_pont + self.eredmenyek.masodik_kor_pont:
            times.append(self.eredmenyek.harmadik_kor_ido + self.eredmenyek.masodik_kor_ido)
        if self.osszpont() == self.eredmenyek.harmadik_kor_pont + self.eredmenyek.elso_kor_pont:
            times.append(self.eredmenyek.harmadik_kor_ido + self.eredmenyek.elso_kor_pont)
        return (min(times))
        
        
