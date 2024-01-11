def beolvas_fajlbol(fajlnev):
    adatok = []
    try:
        with open(fajlnev, 'r', encoding='utf-8') as fajl:
            for sor in fajl:
                adatok.append(sor.strip().split(';'))
    except FileNotFoundError:
        print("A megadott fájl nem található.")
    return adatok

def listaz_adatok(adatok):
    for adat in adatok:
        print(";".join(adat))

def kiir_fajlba(adatok, kimeneti_fajlnev):
    with open(kimeneti_fajlnev, 'w', encoding='utf-8') as fajl:
        for adat in adatok:
            fajl.write(";".join(adat) + '\n')

def idotartomanyban_listaz(adatok, kezdo_ev, vegso_ev):
    for adat in adatok:
        evszam = int(adat[0])
        if kezdo_ev <= evszam <= vegso_ev:
            print(";".join(adat))

def tudastesztfeladat(adatok):
    import random

    evszamok = [adat[0] for adat in adatok]
    veletlen_evszam = random.choice(evszamok)

    helyes_vivmanyok = [adat[1] for adat in adatok if adat[0] == veletlen_evszam]
    veletlen_vivmanytartalom = random.sample(helyes_vivmanyok, min(3, len(helyes_vivmanyok)))

    print(f"Évszám: {veletlen_evszam}")
    for i, vivmany in enumerate(veletlen_vivmanytartalom, start=1):
        print(f"{i}. {vivmany}")

    megadott_valasz = input("Kérlek add meg a helyes vívmány sorszámát: ")
    if megadott_valasz.isdigit() and 1 <= int(megadott_valasz) <= len(veletlen_vivmanytartalom):
        valasztott_vivmany = veletlen_vivmanytartalom[int(megadott_valasz) - 1]
        if valasztott_vivmany in helyes_vivmanyok:
            print("Gratulálok, helyes válasz!")
        else:
            print(f"Sajnálom, a helyes válasz: {', '.join(helyes_vivmanyok)}")
    else:
        print("Hibás bemenet. Kérlek adj meg egy érvényes sorszámot.")

def main():
    fajlnev = "vivmanyok.txt"  # Itt add meg a fájl nevét, vagy módosítsd szükség szerint
    adatok = beolvas_fajlbol(fajlnev)

    while True:
        print("\nMenü:")
        print("1. Minden adat listázása a képernyőre")
        print("2. Minden adat listázása egy fájlba")
        print("3. Adott időtartományban lévő vívmányok összes adatának listázása")
        print("4. Tudástesztfeladat")
        print("0. Kilépés")

        valasztas = input("Válassz egy menüpontot: ")

        if valasztas == "1":
            listaz_adatok(adatok)
        elif valasztas == "2":
            kimeneti_fajlnev = input("Add meg a kimeneti fájl nevét: ")
            kiir_fajlba(adatok, kimeneti_fajlnev)
            print(f"Az adatok ki lettek írva a(z) {kimeneti_fajlnev} fájlba.")
        elif valasztas == "3":
            kezdo_ev = int(input("Add meg a kezdő évszámot: "))
            vegso_ev = int(input("Add meg a végső évszámot: "))
            idotartomanyban_listaz(adatok, kezdo_ev, vegso_ev)
        elif valasztas == "4":
            tudastesztfeladat(adatok)
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Kérlek válassz újra.")

if _name_ == "_main_":
    main()