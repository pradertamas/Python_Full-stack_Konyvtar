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
                print("Beléptél az Könyvtári könyvek lekérdezése menübe")
                print("Az alábbi könyvek vannak állományban:")

            if y == 3:
                y = None
                print("Beléptél az Állományból törlés menübe")
                print("Add meg a könyv számát a törléshez:")

            if y == 4:
                y = None
                print("Visszaléptél a Főmenűbe!")



        if x == 2:
            x = None
            print ("Beléptél a Böngészés menübe")
            y = None
            while y not in [1, 2, 3, 4, 5]:
                print("1. Keresés cím szerint")
                print("2. Keresés szerző szerint")
                print("3. Keresés kiadás éve szerint")
                print("4. Keresés kategória szerint")
                print("5. Vissza a főmenübe")
                try:
                    y = int(input('Válassz a fenti menüpontokból: '))
                    if y not in [1, 2, 3, 4, 5]:
                        print("Érvénytelen választás. Próbáld újra!")
                except ValueError:
                    print("Kérlek, számot adj meg!")
            
            if y == 1:
                y = None
                print("Írd be a keresett könyv címét:")
            
            if y == 2:
                y = None
                print("Írd be a keresett szerző nevét:")

            if y == 3:
                y = None
                print("Írd be a kereséshez a kiadás évét:")
            if y == 4:
                y = None
                print("Írd be a keresett könyv kategóriáját:")

            if y == 5:
                y = None
                print("Visszaléptél a Főmenűbe!")





        if x == 3:
            x = None
            print("Kiléptél a programból!")