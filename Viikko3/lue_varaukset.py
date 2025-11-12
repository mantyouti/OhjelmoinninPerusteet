"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funktioita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varausnumero(varaus):
    numero = varaus[0]
    print(f"Varausnumero: {numero}")
def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")
def hae_paiva(varaus):
    paiva = varaus[2]
    paiva_obj = datetime.strptime(paiva, '%Y-%m-%d')
    print("Päivämäärä:", paiva_obj.strftime('%d.%m.%Y'))
def hae_aloitusaika(varaus):
    aloitusaika = varaus[3]
    muokattu_aika = aloitusaika.replace(":", ".")
    print("Aloitusaika:", muokattu_aika)
def hae_tuntimaara(varaus):
    tuntimaara = int(varaus[4])
    print("Tuntimäärä:", tuntimaara)
def hae_tuntihinta(varaus):
    tuntihinta = float(varaus[5])
    muokattu_tuntihinta = str(tuntihinta).replace(".", ",")
    print("Tuntihinta:", muokattu_tuntihinta, "€")
def laske_kokonaishinta(varaus):
    tuntimaara = int(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = float(tuntimaara) * float(tuntihinta)
    muokattu_kokonaishinta = str(kokonaishinta).replace(".", ",")
    print("Kokonaishinta:", muokattu_kokonaishinta, "€")
def hae_maksettu(varaus):
    maksettu = bool(varaus[6])
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
def hae_kohde(varaus):
    kohde = str(varaus[7]) 
    print("Kohde:", kohde)
def hae_puhelin(varaus):
    puhelin = str(varaus[8])
    print("Puhelin:", puhelin)
def hae_sahkoposti(varaus):
    sahkoposti = str(varaus[9])
    print("Sähköposti:", sahkoposti)

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    # Toteuta loput funktio hae_varaaja(varaus) mukaisesti
    # Luotavat funktiota tekevat tietotyyppien muunnoksen
    # ja tulostavat esimerkkitulosteen mukaisesti

    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)

if __name__ == "__main__":
    main()