"""2. feladat:    összesen 14p szerezhető, a modul neve: sorozat.py
minta:
II/A, B, C:
           	23; 46; 10; 1; 6
II/D, E:
           	Az egyjegyűek száma : 2.
A szamok.txt tartalma:
II/F:
A fejek száma: 2.

A.Írasson ki a konzolra kötőjellel (-) elválasztva 5 lottószámot véletlen számsorozat alapján a mintának megfelelően! (4p)
B.A generált értékeket tárolja lista adatszerkezetben! (1p)
C.A „;” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.Írjon függvényt egyjegyuek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami egyjegyű (1). A visszatérési érték legyen egy egész szám! (3p)
E.A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a szamok.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)"""

vel_lista=[]
import random

def szamok():
    i = 0
    szamok =""
    while i < 5:
        vel = int(random.random()*89) + 1
        vel_lista.append(vel)
        szamok += str(vel)
        if i !=4:
            szamok+=";"
        i+=1

    print(f"II/A,B,C: \n \t {szamok}")

def egyjegyuek_szama():
    i = 0
    darab = 0
    while i < len(vel_lista):
        if vel_lista[i] < 10:
            darab +=1
        i += 1

    return darab
def konzol_kiir():
    print(f"II/D,E : \n \t Az egyjegyűek száma: {egyjegyuek_szama()}")
    print(f"II/F:\n \t A fejek száma : {egyjegyuek_szama()}")

def file_kiir():
    fajl = open("szamok.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\n \t A fejek száma : {egyjegyuek_szama()}")
    fajl.close()








