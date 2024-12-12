def ujkonyv(cim, szerzo, ev, kategoria):
    print("Bent vagy az új könyv adatkezelőben")
    print("Az új könyv adatai: Cím:")
    print(f"Cím: {cim} Szerző: {szerzo} Kiadás éve: {ev} Kategória: {kategoria}")
    
    konyv_adatok = [cim, szerzo, ev, kategoria]
    file = open("konyvek.csv", "a")
    i = 0
    while i < len(konyv_adatok):
        # Írás a fájlba
        if i == 0:  # Csak az első iterációban kezdj egy új sort
            file.write(",".join([str(elem) for elem in konyv_adatok]) + "\n")
        i += 1

    # Fájl bezárása
    file.close()