Könyvtárkezelő program

-------------------------

A program feladata:
Könyvtári könyvek nyilvántartása:
- új könyvek rögzítése
- könyvtári könyvek közötti keresés különböző kategóriákban
- elveszett/megsemmisült példányok jelölhetősége

-------------------------

A program fájlstruktúrája
Mappaszerkezet:
main.py - A program belépési pontja (Felhasználói felület modul)
adatfeldolgozas.py - Az adatfeldolgozó logika
adatkezelo.py - Az adatkezelő logika
konyvek.csv - Az adatok tárolása

-------------------------

Modulok és funkciók
1. Felhasználói felület (UI modul) (Práder Tamás)
Ez a modul kezeli az interakciót a felhasználóval. Meg kell jeleníteni a menüt, be kell kérni az adatokat, és továbbítani kell azokat az adatfeldolgozó modulnak. A válaszokat vissza kell adni a felhasználónak.

Feladatok:

Menü megjelenítése: Ki kell írni a menü opcióit a print() függvény segítségével.
Visszacsatolás megjelenítése: Meg kell jeleníteni az adatfeldolgozó modul által visszaadott adatokat.

2. Adatfeldolgozó modul  (Práder Tamás)
Ez a modul felelős az feldolgozásáért és az adatkezelő modul hívásáért. Az adatokat vissza kell adni a felhasználói felület modulnak feldolgozás után.

Feladatok:
Lekérdezések végrehajtása: Szűrni kell az adatokat a felhasználó igényei szerint.
Törlési logika kezelése: A megsemmisült könyveket jelölni kell, de nem szabad véglegesen törölni.

3. Adatkezelő modul  (Práder Tamás)
Ez a modul felelős az adatok tárolásáért, kezeléséért és visszaadásáért. A CSV-fájl használatával kell kezelni az adatokat.

Feladatok:
Fájl olvasása és írása: Meg kell írni a fájlkezelő függvényeket, amelyek olvassák és írják a CSV-fájlt.
Adatok módosítása: Hozzá kell adni új adatokat, vagy frissíteni kell meglévő adatokat.
Adatok visszaadása: Vissza kell adni a feldolgozó modul számára az adatokat megfelelő formátumban.
Kapcsolódás a modulok között
A felhasználói felület modulnak el kell küldenie a felhasználói inputokat az adatfeldolgozó modulnak.
Az adatfeldolgozó modulnak a megfelelő adatokat be kell kérnie az adatkezelő modulból, és feldolgozás után vissza kell adnia azokat a felhasználói felületnek.
Az adatkezelő modulnak tárolnia kell az adatokat a CSV-fájlban, és vissza kell adnia azokat a feldolgozó modulnak a megfelelő lekérdezésekhez.

----------------------------------

Fejlesztési lépések

Adatkezelő modul fejlesztése:
- Létre kell hozni egy alap CSV-fájlt a könyvek adataival.
- Meg kell írni a fájl beolvasását és írását kezelő függvényeket.

Adatfeldolgozó modul fejlesztése:
- Meg kell írni a függvényeket az adatok validálására, szűrésére és feldolgozására.

Felhasználói felület modul fejlesztése:
- Készíteni kell egy egyszerű terminál alapú menüt.
- Meghívni kell az adatfeldolgozó függvényeket a menüben megadott opciók szerint.

Integráció és tesztelés:
- Ellenőrizni kell, hogy a modulok megfelelően kommunikálnak egymással.
- Tesztelni kell az összes funkciót valós adatbevitel mellett.
