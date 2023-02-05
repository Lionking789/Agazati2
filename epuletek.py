"""3. feladat:    összesen 17p szerezhető, a modul neve: epuletek.py
Az auto.txt forrásállomány, autók adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Készítsen programotautom.pynéven. Olvassa beauto.txtfájlból az auto adatait, tároljaAutoosztály típusúkocsinevű listában a példányokat.
A megoldás mintája:
III/Flotta:
Autók száma: 7.
III/Legfiatalabb
A legfiatalabb autó: Seat Ibiza(2011))


A.Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a auto.txt fájlból a autók adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.Készíts függvényt flotta néven, amely visszaadja az autók számát a mintának megfelelően, majd írasd ki  a konzolra a mintának megfelelően! (2p)
C.Add meg az legfiatalabb autó nevét a mintának megfelelően a konzolra írva!! (4p)
D.Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)"""

from Auto import Auto
auto_lista=[]


def beolvas():
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    #print(sorok)

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        i += 1
    return auto_lista

def auto_szama():
    return len(auto_lista)

def legfitalabb_auto():
    i = 0
    fiatalabb = auto_lista[0]

    while i < len(auto_lista):
        if auto_lista[i].datum > fiatalabb.datum:
            fiatalabb = auto_lista[i]
        i += 1
    return fiatalabb







