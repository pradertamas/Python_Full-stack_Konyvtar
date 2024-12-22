def ujkonyv_ak(konyv_adatok):
    file = open("konyvek.csv", "a", encoding="utf-8")
    file.write(f"{konyv_adatok[0]},{konyv_adatok[1]},{konyv_adatok[2]},{konyv_adatok[3]},1\n")
    file.close()


def konyvtar_lista_ak():
    with open("konyvek.csv","r", encoding="utf-8") as f:
        konyvek=f.read().splitlines()
    return konyvek

def torles_ak(konyv_lista):
    with open("konyvek.csv","w", encoding="utf-8") as f:
        f.write(f"cim,szerzo,ev,kategoria,aktiv\n")
        for konyv in konyv_lista:
            f.write(f'{konyv["cim"]},{konyv["szerzo"]},{konyv["ev"]},{konyv["kategoria"]},{konyv["aktiv"]}\n')
    