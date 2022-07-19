#napisati regex koji vraca podudaranje ukoliko se unese string
#počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
#String mora sadržavati bar jedan broj između 0 i 5 i razmak.


import re

regex = "^m[0-5]+\s.*r$"

while 1:
    unos = input("Unesite ime:")
    rezultat = re.match(regex,unos)
    if rezultat:
        break
    else:
        print("Pogresan unos!")
print("Uspješno")
