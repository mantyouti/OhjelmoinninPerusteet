# Copyright (c) 2025 Ville Heikkiniemi
# 
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.


from datetime import datetime, date # Tuodaan datetime- ja date-luokat datetime-kirjastosta

def muunna_tiedot(kulutusTuotanto: list) -> list: # Muuntaa tietorivin oikeisiin tietotyyppeihin
    muutettu_tietorivi = [] # Lista muunnetuista tiedoista
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0])) # Muuntaa päivämäärä- ja aikamerkinnän datetime-objektiksi
    muutettu_tietorivi.append(int(kulutusTuotanto[1])) # Muuntaa muut sarakkeet kokonaisluvuiksi
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
    return muutettu_tietorivi # Palauttaa muunnetun tietorivin listana

def lue_data(tiedoston_nimi: str) -> list: #Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä.
    kulutusTuotantoTiedot = [] # Lista, johon tallennetaan kaikki tiedot
    with open(tiedoston_nimi, "r", encoding="utf-8") as f: # Avaa tiedoston lukemista varten
        next(f) # Ohitetaan otsikkorivi
        for kulutusTuotantoTieto in f: # Käydään tiedoston rivit läpi
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip() # Poistetaan rivin alusta ja lopusta ylimääräiset välilyönnit ja rivinvaihdot
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';') # Pilkotaan rivi sarakkeisiin puolipisteen kohdalta
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet)) # Muunnetaan sarakkeet oikeisiin tietotyyppeihin ja lisätään lista päälistaan
    return kulutusTuotantoTiedot #palauttaa listan, jossa jokainen alkio on lista yhdestä rivistä

def paivantiedot(paiva: str, lukemat: list) -> list: # Laskee annetun päivän kulutukset ja tuotannot vaiheittain
    
    lasketutTiedot = [] # Lista, johon tallennetaan lasketut tiedot
    kulutus1vaihe = kulutus2vaihe = kulutus3vaihe = 0 # Alustetaan kulutusmuuttujat
    tuotanto1vaihe = tuotanto2vaihe = tuotanto3vaihe = 0 # Alustetaan tuotantomuuttujat
    pv, kk, vuosi = map(int, paiva.split('.')) # Pilkotaan päivämäärä osiin ja muunnetaan kokonaisluvuiksi
    for lukema in lukemat: # Käydään läpi kaikki lukemat
        if lukema[0].date() == date(vuosi, kk, pv): # Verrataan päivämääriä
            kulutus1vaihe += lukema[1] # Lisätään kulutus ja tuotanto vastaaviin muuttujiin
            kulutus2vaihe += lukema[2] 
            kulutus3vaihe += lukema[3]
            tuotanto1vaihe += lukema[4]
            tuotanto2vaihe += lukema[5]
            tuotanto3vaihe += lukema[6]

    lasketutTiedot.append(kulutus1vaihe/1000)  # Muutetaan Wh -> kWh jakamalla 1000:lla
    lasketutTiedot.append(kulutus2vaihe/1000)
    lasketutTiedot.append(kulutus3vaihe/1000)
    lasketutTiedot.append(tuotanto1vaihe/1000)
    lasketutTiedot.append(tuotanto2vaihe/1000)
    lasketutTiedot.append(tuotanto3vaihe/1000)
    return lasketutTiedot

def main(): #ohjelman pääfunktio, lukee datan, laskee yhteenvedot ja tulostaa ne

    lukemat = lue_data("viikko42.csv") # kutsuu lue_data-funktiota ja tallentaa paluuarvon muuttujaan lukemat
    print()
    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)") #tulostaa otsikon
    print()
    print("Päivä            Pvm             Kulutus [kWh]                 Tuotanto [kWh]")
    print("                 pv.kk.vvvv      v1      v2      v3             v1     v2       v3")
    print("--------------------------------------------------------------------------------------------")


    maanantainlukemat = paivantiedot("13.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle csv tiedostosta lukemina
    tiistainlukemat = paivantiedot("14.10.2025", lukemat) 
    keskiviikonlukemat = paivantiedot("15.10.2025", lukemat)
    torstainlukemat = paivantiedot("16.10.2025", lukemat)
    perjantainlukemat = paivantiedot("17.10.2025", lukemat)
    lauantainlukemat = paivantiedot("18.10.2025", lukemat)
    sunnuntainlukemat = paivantiedot("19.10.2025", lukemat)


    maanantainlukemat = paivantiedot("13.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle ja muuntaa luvun desimaaliluvuksi pilkulla
    print(f"Maanantai \t 13.10.2025 \t", f"{maanantainlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {maanantainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {maanantainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{maanantainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {maanantainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {maanantainlukemat[5]:.2f}".replace('.', ','))

    tiistainlukemat = paivantiedot("14.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"Tiistai \t 14.10.2025 \t", f"{tiistainlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {tiistainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {tiistainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{tiistainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {tiistainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {tiistainlukemat[5]:.2f}".replace('.', ','))

    keskiviikonlukemat = paivantiedot("15.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"keskiviikko \t 15.10.2025 \t", f"{keskiviikonlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {keskiviikonlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {keskiviikonlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{keskiviikonlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {keskiviikonlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {keskiviikonlukemat[5]:.2f}".replace('.', ','))

    torstainlukemat = paivantiedot("16.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"torstai \t 16.10.2025 \t {f'{torstainlukemat[0]:.2f}'.replace('.', ',')}", end='\t')
    print(f" {torstainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {torstainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{torstainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {torstainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {torstainlukemat[5]:.2f}".replace('.', ','))

    perjantainlukemat = paivantiedot("17.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"perjantai \t 17.10.2025 \t", f"{perjantainlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {perjantainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {perjantainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{perjantainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {perjantainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {perjantainlukemat[5]:.2f}".replace('.', ','))

    lauantainlukemat = paivantiedot("18.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"lauantai \t 18.10.2025 \t", f"{lauantainlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {lauantainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {lauantainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{lauantainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {lauantainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {lauantainlukemat[5]:.2f}".replace('.', ','))

    sunnuntainlukemat = paivantiedot("19.10.2025", lukemat) # Palauttaa kulutukset annetulle päivälle
    print(f"sunnuntai \t 19.10.2025 \t", f"{sunnuntainlukemat[0]:.2f}".replace('.', ','), end='\t')
    print(f" {sunnuntainlukemat[1]:.2f}".replace('.', ','), end='\t')
    print(f" {sunnuntainlukemat[2]:.2f}".replace('.', ','), end='\t')
    print(f" \t{sunnuntainlukemat[3]:.2f}".replace('.', ','), end='\t')
    print(f" {sunnuntainlukemat[4]:.2f}".replace('.', ','), end='\t')
    print(f" {sunnuntainlukemat[5]:.2f}".replace('.', ','))

    print()
    print()

if __name__ == "__main__": 
    main() # Kutsuu pääohjelman