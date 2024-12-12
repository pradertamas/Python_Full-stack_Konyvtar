import adatfeldolgozas
import adatkezelo

print("Ez egy könytarkezelő program")

while True:
        print("1. Adminisztráció")
        print("2. Böngészés")
        print("3. Kilépés")    
        valasztas = input("Válassz a fenti menüpontokból: ")
        
        if valasztas == "1":
            print ("Beléptél az Admin menübe")
            
            while True:
                print("1. Új könyv felvétele")
                print("2. Könyvtári könyvek lekérdezései")
                print("3. Állományból törlés")
                print("4. Visszalépés")                
                valasztas = input("Válassz a fenti menüpontokból: ")

                if valasztas == "1":
                    print ("Beléptél az Új könyv felvétele menübe")
                    cim = input("Add meg a könyv címét: ")
                    szerzo = input("Add meg a könyv szerzőjét: ")
                    ev = int(input("Add meg a könyv kiadásának évét: "))
                    kategoria = input("Add meg a könyv kategóriáját: ")
                    adatkezelo.ujkonyv(cim, szerzo, ev, kategoria)
                elif valasztas == "2":
                    print("Beléptél az Könyvtári könyvek lekérdezése menübe")
                    print("Az alábbi könyvek vannak állományban:")

                    #----------ez kiírja a könyvek listáját, ebből függvényt kell csinálni
                    konyv_lista=[]

                    with open("konyvek.csv","r", encoding="utf-8") as f:
                        sorok=f.read().splitlines()
                        for sor in sorok[1::]:
                            adat=sor.strip().split(",")
                            
                            konyvtar={}
                            konyvtar["cim"]=adat[0]
                            konyvtar["szerzo"]=adat[1]
                            konyvtar["ev"]=int(adat[2])
                            konyvtar["kategoria"]=adat[3]
                            
                            konyv_lista.append(konyvtar)

                    print(f"{'Sorszám':<8} {'Cím':<25} {'Szerző':<20} {'Év':<5} {'Kategória':<15}")
                    print("=" * 71)

                    sorszam = 1
                    for k in konyv_lista:
                        print(f"{sorszam:<8} {k['cim']:<25} {k['szerzo']:<20} {k['ev']:<5} {k['kategoria']:<15}")
                        sorszam += 1
                    #----------ez kiírja a könyvek listáját

                elif valasztas == "3":
                    print("Beléptél az Állományból törlés menübe")
                    
                    print("")
                    sorszam = int(input("Add meg a könyv számát a törléshez: "))
                elif valasztas == "4":
                    print("Visszaléptél a Főmenűbe!")
                    break
                else:
                    print("Érvénytelen választás, próbáld újra!")

        elif valasztas == "2":
            print("Beléptél a Böngészés menübe")
            while True:
                print("1. Keresés cím szerint")
                print("2. Keresés szerző szerint")
                print("3. Keresés kiadás éve szerint")
                print("4. Keresés kategória szerint")
                print("5. Visszalépés")
                valasztas = input("Válassz a fenti menüpontokból: ")

                if valasztas == "1":
                    cim = input("Add meg a keresett könyv címét: ")
                elif valasztas == "2":
                    szerzo = input("Add meg a keresett könyv szerzőjét: ")
                elif valasztas == "3":
                    ev = int(input("Add meg a keresett könyv kiadásának évét: "))
                elif valasztas == "4":
                    kategoria = input("Add meg a keresett könyv kategóriáját: ")
                elif valasztas == "5":
                    print("Visszaléptél a Főmenűbe!")
                    break
                else:
                    print("Érvénytelen választás, próbáld újra!")


        elif valasztas == "3":
            print("Kiléptél a programból.")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")