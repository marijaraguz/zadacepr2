#rekurzivna funkcija koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.

rijec = input("Unesite rijec:")
def obrnuto_rekurzija(rijec):
        if len(rijec)==1:
            return rijec
        return obrnuto_rekurzija(rijec[1::]) + rijec[0]

print(obrnuto_rekurzija(rijec))
