# Copyright (c) 2025 Ville Heikkiniemi
# 
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date
        
def lue_data(tiedoston_nimi: str) -> list: # Funktio lukee tiedoston ja palauttaa tietokannan listana
        tietokanta = []
        with open(tiedoston_nimi, "r", encoding="utf-8") as f:
                next(f)  # Otetaan kenttien esittelytiedot pois
                for tietue in f: # Käydään tiedosto rivi riviltä läpi
                        tietue = tietue.strip() # Poistetaan rivin lopusta ylimääräiset merkit
                        tietue = tietue.split(";") # Pilkotaan rivi osiin puolipisteen kohdalta
                        tietokanta.append(muunna_tiedot(tietue)) # Muunnetaan tiedot oikeaan muotoon ja lisätään tietokantaan
        return tietokanta

def raportti_tiedostoon(raportti: str): # Funktio kirjoittaa raportin tiedostoon
        with open("raportti.txt", "w", encoding="utf-8") as f:
                f.write(str((raportti)))

def muunna_tiedot(tietue: list) -> list: # Funktio muuntaa tiedot oikeaan muotoon

        return [
    datetime.fromisoformat(tietue[0]).date(),
    float(tietue[1].replace(',', '.')),
    float(tietue[2].replace(',', '.')),
    float(tietue[3].replace(',', '.')),
]
def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) -> str: # Funktio luo raportin annetulta aikaväliltä
        alkupv = alkupaiva.split('.')[0]
        alkukk = alkupaiva.split('.')[1]
        alkuvv = alkupaiva.split('.')[2]
        alku = datetime(int(alkuvv), int(alkukk), int(alkupv)).date()
        loppupv = loppupaiva.split('.')[0]
        loppukk = loppupaiva.split('.')[1]
        loppuvv = loppupaiva.split('.')[2]
        loppu = datetime(int(loppuvv), int(loppukk), int(loppupv)).date()
        kulutus = 0
        tuotanto = 0
        lampotila = 0
        tietue_lkm = 0
        for tietue in tietokanta:
            if alku <= tietue[0] <= loppu:
                kulutus += tietue[1]
                tuotanto += tietue[2]
                lampotila += tietue[3]
                tietue_lkm += 1
        raportti = "------------------------------------------------\n"
        raportti += f"-Raportti ajalta {alkupaiva} - {loppupaiva}\n"
        raportti += f"-Aikavälin kokonaiskulutus {kulutus:.2f} kWh\n".replace(',', '.') 
        raportti += f"-Aikavälin kokonaistuotanto {tuotanto:.2f} kWh\n".replace(',', '.')
        raportti += f"-Aikavälin keskimääräinen lämpötila {lampotila/tietue_lkm:.2f} °C\n".replace(',', '.')
        raportti += "-----------------------------------------------\n"
        return raportti

def raportti_kuukausi(kuukausi: int, tietokanta: list) -> str: # Funktio luo raportin annetulta kuukaudelta
        kk = int(kuukausi)
        kulutus = 0
        tuotanto = 0
        lampotila = 0
        tietue_lkm = 0
        for tietue in tietokanta:
            if tietue[0].month == kk:
                kulutus += tietue[1]
                tuotanto += tietue[2]
                lampotila += tietue[3]
                tietue_lkm += 1
        raportti = "------------------------------------------------\n"
        raportti += f"-Raportti kuukaudelta {kuukausi}\n"
        raportti += f"-Kuukauden kokonaiskulutus {kulutus:.2f} kWh\n".replace(',', '.') 
        raportti += f"-Kuukauden kokonaistuotanto {tuotanto:.2f} kWh\n".replace(',', '.')
        raportti += f"-Kuukauden keskimääräinen lämpötila {lampotila/tietue_lkm:.2f} °C\n".replace(',', '.')
        raportti += "-----------------------------------------------\n"
        return raportti

def raportti_vuosi(vuosi: int, tietokanta: list) -> str: # Funktio luo raportin vuodelta 2025
        kulutus = 0
        tuotanto = 0
        lampotila = 0
        tietue_lkm = 0
        for tietue in tietokanta:
            if tietue[0].year == vuosi:
                kulutus += tietue[1]
                tuotanto += tietue[2]
                lampotila += tietue[3]
                tietue_lkm += 1
        raportti = "------------------------------------------------\n"
        raportti += f"-Raportti vuodelta {vuosi}\n"
        raportti += f"-Vuoden kokonaiskulutus {kulutus:.2f} kWh\n".replace(',', '.') 
        raportti += f"-Vuoden kokonaistuotanto {tuotanto:.2f} kWh\n".replace(',', '.')
        raportti += f"-Vuoden keskimääräinen lämpötila {lampotila/tietue_lkm:.2f} °C\n".replace(',', '.')
        raportti += "-----------------------------------------------\n"
        return raportti

def main(): # Pääohjelma
        # luetaan data tiedostosta:
    kulutusTuotanto2025 = lue_data("2025.csv")
    #print (len(kulutusTuotanto2025))

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        eka_valinta = int(input("Anna valintasi (1-4): "))
        if eka_valinta == 1: # Kutsu funktiota, joka käsittelee päiväkohtaisen yhteenvedon
                alkupaiva = input("Anna alkupäivä (pv.kk.vvvv):")
                loppupaiva = input("Anna loppupäivä (pv.kk.vvvv):")
                raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutusTuotanto2025)
                print(raportti)
        elif eka_valinta == 2: # Kutsu funktiota, joka käsittelee kuukausikohtaisen yhteenvedon
                kuukausi = int(input("Anna kuukausi (1-12):"))
                raportti = raportti_kuukausi(kuukausi, kulutusTuotanto2025)
                print(raportti)

        elif eka_valinta == 3: # Kutsu funktiota, joka käsittelee vuosikulutuksen yhteenvedon
                vuosi = 2025
                raportti = raportti_vuosi(vuosi, kulutusTuotanto2025)
                print(raportti)

        if eka_valinta == 4:
                print("Lopetetaan ohjelma.") 

        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toka_valinta = int(input("Anna valintasi (1-3): "))
        if toka_valinta == 1:
                raportti_tiedostoon(raportti)
                print("Raportti kirjoitettu tiedostoon raportti.txt")
        elif toka_valinta == 2:
                print("Valitse raporttityyppi:")
                print("1) Päiväkohtainen yhteenveto aikaväliltä")
                print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
                print("3) Vuoden 2025 kokonaisyhteenveto")
                print("4) Lopeta ohjelma")
                continue
        
        elif toka_valinta == 3:
                print("Lopetetaan ohjelma.")
                break
        continue

print("----------------------")

if __name__ == "__main__":
    main()