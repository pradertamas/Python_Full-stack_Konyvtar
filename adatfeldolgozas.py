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