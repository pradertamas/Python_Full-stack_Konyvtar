import adatfeldolgozas

print("Ez egy könytarkezelő program")
print("")

while True:
        print("1. Adminisztráció")
        print("2. Böngészés")
        print("3. Kilépés")    
        valasztas = input("Válassz a fenti menüpontokból: ")
        
        if valasztas == "1":
            print ("Beléptél az Admin menübe")
            print("")
            
            while True:
                print("1. Új könyv felvétele")
                print("2. Könyvtári állomány lekérdezése")
                print("3. Állományból törlés")
                print("4. Visszalépés")                
                valasztas = input("Válassz a fenti menüpontokból: ")

                if valasztas == "1":
                    print ("Beléptél az Új könyv felvétele menübe")
                    print("")
                    cim = input("Add meg a könyv címét: ")
                    szerzo = input("Add meg a könyv szerzőjét: ")
                    ev = int(input("Add meg a könyv kiadásának évét: "))
                    kategoria = input("Add meg a könyv kategóriáját: ")
                    print("Az új könyv adatai: Cím:")
                    print(f"Cím: {cim} Szerző: {szerzo} Kiadás éve: {ev} Kategória: {kategoria}")
                    adatfeldolgozas.ujkonyv_af(cim, szerzo, ev, kategoria)
                    print("Az új könyv rögzítése sikeres!")
                elif valasztas == "2":
                    print("Beléptél az Könyvtári állomány lekérdezése menübe")
                    print("")
                    print("Az alábbi könyvek vannak állományban:")

                    print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15} {'Aktív?':<10}")
                    print("=" * 106)
                    sorszam = 1
                    for k in adatfeldolgozas.konyvtar_lista_af():
                        print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15} {('igen' if k['aktiv'] == 1 else 'nem'):<10}")
                        sorszam += 1
                    print("")

                elif valasztas == "3":
                    print("Beléptél az Állományból törlés menübe")
                    print("")
                    print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15} {'Aktív?':<10}")
                    print("=" * 106)
                    sorszam = 1
                    for k in adatfeldolgozas.konyvtar_lista_af():
                        print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15} {('igen' if k['aktiv'] == 1 else 'nem'):<10}")
                        sorszam += 1
                    print("")
                    sorszam = int(input("A felti listából add meg a könyv számát a törléshez: "))
                    adatfeldolgozas.torles_af(sorszam)
                    print("Az aktív állományból törlésre került a könyv.")
                    print("")
                elif valasztas == "4":
                    print("Visszaléptél a Főmenűbe!")
                    print("")
                    break
                else:
                    print("Érvénytelen választás, próbáld újra!")

        elif valasztas == "2":
            print("Beléptél a Böngészés menübe")
            print("")
            while True:
                print("1. Keresés cím szerint")
                print("2. Keresés szerző szerint")
                print("3. Keresés kategória szerint")
                print("4. A teljes állomány listázása")
                print("5. Visszalépés")
                valasztas = input("Válassz a fenti menüpontokból: ")

                if valasztas == "1":
                    cim = input("Add meg a keresett könyv címét pontosan: ")
                    if adatfeldolgozas.ker_cim_af(cim) == []:
                        print("")
                        print("Nincs ilyen című könyv!")
                        print("")
                    else:
                        print("A cím szerinti keresés eredménye:")
                        print("")
                        print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15}")
                        print("=" * 106)
                        sorszam = 1
                        for k in adatfeldolgozas.ker_cim_af(cim):
                            print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15}")
                            sorszam += 1
                        print("")

                elif valasztas == "2":
                    szerzo = input("Add meg a keresett könyv szerzőjét: ")
                    if adatfeldolgozas.ker_szerzo_af(szerzo) == []:
                        print("")
                        print("Nincs ilyen szerzőtől könyv!")
                        print("")
                    else:
                        print("A szerző szerinti keresés eredménye:")
                        print("")
                        print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15}")
                        print("=" * 106)
                        sorszam = 1
                        for k in adatfeldolgozas.ker_szerzo_af(szerzo):
                            print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15}")
                            sorszam += 1
                        print("")

                elif valasztas == "3":
                    kategoria = input("Add meg a keresett könyv kategóriáját: ")
                    if adatfeldolgozas.ker_kategoria_af(kategoria) == []:
                        print("")
                        print("Nincs ilyen kategóriájú könyv!")
                        print("")
                    else:
                        print("A kategória szerinti keresés eredménye:")
                        print("")
                        print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15}")
                        print("=" * 106)
                        sorszam = 1
                        for k in adatfeldolgozas.ker_kategoria_af(kategoria):
                            print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15}")
                            sorszam += 1
                        print("")

                elif valasztas == "4":
                    print("5. A teljes állomány:")
                    print("")
                    print(f"{'Sorszám':<8} {'Cím':<35} {'Szerző':<30} {'Év':<5} {'Kategória':<15}")
                    print("=" * 106)
                    sorszam = 1
                    for k in adatfeldolgozas.bongeszes_af():
                        print(f"{sorszam:<8} {k['cim']:<35} {k['szerzo']:<30} {k['ev']:<5} {k['kategoria']:<15}")
                        sorszam += 1
                    print("")
                elif valasztas == "5":
                    print("Visszaléptél a Főmenűbe!")
                    print("")
                    break
                else:
                    print("Érvénytelen választás, próbáld újra!")
                    print("")


        elif valasztas == "3":
            print("Kiléptél a programból.")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")
            print("")