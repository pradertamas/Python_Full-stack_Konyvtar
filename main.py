import adatfeldolgozas
import adatkezelo

print("Ez egy könytarkezelő program")

x = None

while x not in [1, 2, 3]:

    x = None
    while x not in [1, 2, 3]:
        print("1. Adminisztráció")
        print("2. Böngészés")
        print("3. Kilépés")
        try:
            x = int(input('Válassz a fenti menüpontokból: '))
            if x not in [1, 2, 3]:
                print("Érvénytelen választás. Próbáld újra!")
        except ValueError:
            print("Kérlek, számot adj meg!")


    if x == 1:
        x = None
        print ("Beléptél az Admin menübe")
        y = None
        while y not in [1, 2, 3, 4]:
            print("1. Új könyv felvétele")
            print("2. Könyvtári könyvek lekérdezései")
            print("3. Állományból törlés")
            print("4. Vissza a főmenübe")
            try:
                y = int(input('Válassz a fenti menüpontokból: '))
                if y not in [1, 2, 3, 4]:
                    print("Érvénytelen választás. Próbáld újra!")
            except ValueError:
                print("Kérlek, számot adj meg!")
        
        if y == 1:
            y = None
            print("Beléptél az Új könyv felvétele menübe")
            cim = input("Add meg a könyv címét: ")
            szerzo = input("Add meg a könyv szerzőjét: ")
            ev = int(input("Add meg a könyv kiadásának évét: "))
            kategoria = input("Add meg a könyv kategóriáját: ")
            adatkezelo.ujkonyv(cim, szerzo, ev, kategoria)
            
        if y == 2:
            y = None
            print("Beléptél az Könyvtári könyvek lekérdezései menübe")

        if y == 3:
            y = None
            print("Beléptél az Állományból törlés menübe")

        if y == 4:
            y = None
            print("Visszaléptél a Főmenűbe!")



if x == 2:
    x = None
    print ("Beléptél a Böngészés menübe")

if x == 3:
    x = None
    print("Kiléptél a programból!")