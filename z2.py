def ocjena (bodovi):
    if bodovi < 50:
        return "Nedovoljan"
    elif bodovi < 65:
        return "Dovoljan"
    elif bodovi < 80:
        return "Dobar"
    elif bodovi < 90:
        return "Vrlo dobar"
    else:
        return "Odličan"


from csv import reader

with open("rezultati.csv","r",encoding="utf")as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple,csv_reader))

novirez = []
for ime,prezime,bodovi in studenti:
    novirez.append((prezime,ime,bodovi))
print(novirez)

#for i in novirez:
#    print(i)

novirez.sort()
print(novirez)
print("--------------------------------")
popis = []

for student in novirez:
    rjecnik = {}
    rjecnik["prezime"]= student[0]
    rjecnik["ime"]=student[1]
    rjecnik["ocjena"]=ocjena(int(student[2]))
    popis.append(rjecnik)
print(popis)
popis2 = []
for student in popis:
    popis2.append((student["prezime"],student["ime"],student["ocjena"]))
print("--------------------------------------------------------------")
print(popis2)

print("-----------------------")

for prezime,ime,bodovi in popis2:
    print(prezime,ime,bodovi)
