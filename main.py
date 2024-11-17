print("Ez egy könytarkezelő program")

x = 0

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
    print ("Beléptél az Admin menübe")

if x == 2:
    print ("Beléptél a Böngészés menübe")

if x == 3:
    print("Kiléptél a programból!")