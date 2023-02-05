"""I/A:
Autó  neve: Opel Corsa
Gyártási dátum: 2022

I/B:
Ez az Opel Corsa átlagos korú.

A. Kérje be az alábbi adatokat a fenti mintának megfelelően:
Autó  neve és gyártás éve (2p)
B. A program az adatbekérés után írasson ki egy szöveget az alábbiak alapján!
 Amennyiben az autó gyártási éve ez évi, akkor írja ki, „friss gyártás”.
  Amennyiben 2000 előtt gyártották az autót, írja ki: „öreg autó”
 Minden más esetben: „Átlagos korú”. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)"""

def auto():
    nev = input("Autó neve: ")
    datum = int(input("Gyártási dátum: "))

    if datum == 2022:
        print("friss gyártás")

    elif datum < 2000:
        print("öreg autó")

    else:
        print("Átlagos korú")

    print(f"I/A \n \t Autó neve: {nev} \n \t Gyártási dátum: {datum}")
    print("I/B: \n \t Ez az Opel Corsa átlagos korú")









