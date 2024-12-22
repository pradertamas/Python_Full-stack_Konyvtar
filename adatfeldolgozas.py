import adatkezelo

def ujkonyv_af(cim, szerzo, ev, kategoria):
    konyv_adatok = [cim, szerzo, ev, kategoria]    
    adatkezelo.ujkonyv_ak (konyv_adatok)

def konyvtar_lista_af():
    konyv_lista=[]

    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        konyv_lista.append(
            {
            "cim" : adat[0],
            "szerzo" : adat[1],
            "ev" : int(adat[2]),
            "kategoria" : adat[3],
            "aktiv" : int(adat[4])
            }
        )

    return konyv_lista

def torles_af(sorszam):
    konyv_lista=[]
    sor = sorszam-1
    i = 0
    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        
        if i == sor:
            konyv_lista.append(
            {
            "cim" : adat[0],
            "szerzo" : adat[1],
            "ev" : int(adat[2]),
            "kategoria" : adat[3],
            "aktiv" : "0"
            }
        )
        else:
            konyv_lista.append(
                {
                "cim" : adat[0],
                "szerzo" : adat[1],
                "ev" : int(adat[2]),
                "kategoria" : adat[3],
                "aktiv" : int(adat[4])
                }
            )
        i += 1

    #print(f'{konyv_lista[sor]["cim"]},{konyv_lista[sor]["szerzo"]},{konyv_lista[sor]["ev"]},{konyv_lista[sor]["kategoria"]},{konyv_lista[sor]["aktiv"]}')
    adatkezelo.torles_ak(konyv_lista)

def bongeszes_af():
    bongeszesi_lista=[]

    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        if int(adat[4]) == 1:
            bongeszesi_lista.append(
                {
                "cim" : adat[0],
                "szerzo" : adat[1],
                "ev" : int(adat[2]),
                "kategoria" : adat[3]
                #"aktiv" : int(adat[4])
                }
            )
    return bongeszesi_lista

def ker_cim_af(cim):
    keresett_konyv=[]

    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        if cim.lower() in adat[0].lower() and int(adat[4]) == 1:
            keresett_konyv.append(
                {
                "cim" : adat[0],
                "szerzo" : adat[1],
                "ev" : int(adat[2]),
                "kategoria" : adat[3]
                #"aktiv" : int(adat[4])
                }
            )
    return keresett_konyv

def ker_szerzo_af(szerzo):
    keresett_konyv=[]

    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        if szerzo.lower() in adat[1].lower() and int(adat[4]) == 1:
            keresett_konyv.append(
                {
                "cim" : adat[0],
                "szerzo" : adat[1],
                "ev" : int(adat[2]),
                "kategoria" : adat[3]
                #"aktiv" : int(adat[4])
                }
            )
    return keresett_konyv

def ker_kategoria_af(kategoria):
    keresett_konyv=[]

    for konyv in adatkezelo.konyvtar_lista_ak()[1::]:
        adat=konyv.strip().split(",")
        if kategoria.lower() in adat[3].lower() and int(adat[4]) == 1:
            keresett_konyv.append(
                {
                "cim" : adat[0],
                "szerzo" : adat[1],
                "ev" : int(adat[2]),
                "kategoria" : adat[3]
                #"aktiv" : int(adat[4])
                }
            )
    return keresett_konyv