"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

import datetime


def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    print(varaus)

    # Kokeile näitä
    #print(varaus.split('|'))
    varausId = int(varaus.split('|')[0])
    print("Varausnumero", varausId)
    varaaja = str(varaus.split('|')[1])
    print("Varaaja:", varaaja)
    paiva = varaus.split('|')[2]
    from datetime import datetime
    paiva_obj = datetime.strptime(paiva, '%Y-%m-%d')
    print("Päivämäärä:", paiva_obj.strftime('%d.%m.%Y'))
    aloitusaika = varaus.split('|')[3]
    muokattu_aika = aloitusaika.replace(":", ".")
    print("Aloitusaika:", muokattu_aika)
    tuntimaara = int(varaus.split('|')[4])
    print("Tuntimäärä:", tuntimaara)
    tuntihinta = float(varaus.split('|')[5])
    print("Tuntihinta:", tuntihinta, "€")
    kokonaishinta = float(tuntimaara) * float(tuntihinta)
    print("Kokonaishinta:", kokonaishinta, "€")
    maksettu = bool(varaus.split('|')[6])
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    kohde = str(varaus.split('|')[7]) 
    print("Kohde:", kohde)
    puhelin = str(varaus.split('|')[8])
    print("Puhelin:", puhelin)
    sahkoposti = str(varaus.split('|')[9])
    print("Sähköposti:", sahkoposti)


    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()