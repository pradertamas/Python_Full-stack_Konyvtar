print("Ez egy könytarkezelő program")

x = 0

while x != 1 and x != 2 and x != 3:
    print("1. Adminisztráció")
    print("2. Böngészés")
    print("3. Kilépés")
    x = int(input('Válassz a fenti menüpontokból:'))

if x == 1:
    print ("Beléptél az Admin menübe")

if x == 2:
    print ("Beléptél a Böngészés menübe")
