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


# i = 0
# while i < len(konyv_lista):
#     print("Könyv sorszáma: ", i+1, konyv_lista[i], len(konyv_lista[i]))
#     i = i + 1






# konyv_lista=[]

# with open("konyvek.csv","r", encoding="utf-8") as f:
#     sorok=f.read().splitlines()
#     for sor in sorok[1::]:
#         adat=sor.strip().split(",")
        
#         konyvtar={}
#         konyvtar["cim"]=adat[0]
#         konyvtar["szerzo"]=adat[1]
#         konyvtar["ev"]=int(adat[2])
#         konyvtar["kategoria"]=adat[3]
#         konyv_lista.append(konyvtar)

# print(konyv_lista)
