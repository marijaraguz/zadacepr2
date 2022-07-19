#Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
#Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
#X predstavlja bilo koji broj, taj broj ne mora postojati (može biti samo iprezime@sum.ba).
#Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.




import re


regex1 ="^[a-z]+\.[a-z]+@fpmoz.sum.ba$"
regex2 ="^[a-z]{1,2}[a-z]+[0-9]*@sum.ba$"

while 1:
    unos1 = input("Unesite mail:")
    unos2 = input("Unesite eduId:")
    rezultat1 = re.match(regex1,unos1)
    rezultat2 = re.match(regex2,unos2)
    if rezultat1 and rezultat2 :
        break
    else:
        print("Pogresan unos!")
print("Ispravan unos")
