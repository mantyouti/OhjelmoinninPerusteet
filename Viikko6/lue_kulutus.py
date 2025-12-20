# Copyright (c) 2025 Ville Heikkiniemi
# 
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date 

def main(): """Ohjelman pääfunktio: kysyy aikavälin ja tulostaa/vie tiedostoon kulutus- ja tuotantoraportteja."""

print("Valitse raporttityyppi:")
print("1) Päiväkohtainen yhteenveto aikaväliltä")
print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
print("3) Vuoden 2025 kokonaisyhteenveto")
print("4) Lopeta ohjelma")
        
valinta = int(input("Anna valintasi (1-4): "))
if valinta == 1: # Kutsu funktiota, joka käsittelee päiväkohtaisen yhteenvedon
        alkupaiva = input("Anna alkupäivä (pv.kk.vvvv):")
        loppupaiva = input("Anna loppupäivä (pv.kk.vvvv):")
                # Kutsu funktiota, joka käsittelee päiväkohtaisen yhteenvedon aikaväliltä alkupäivä - loppupäivä
        print(alkupaiva, loppupaiva)
if valinta == 2: # Kutsu funktiota, joka käsittelee kuukausikohtaisen yhteenvedon
        vuosi = int(input("Anna vuosi (vvvv):"))
        kuukausi = int(input("Anna kuukausi (1-12):"))
                # Kutsu funktiota, joka käsittelee kuukausikohtaisen yhteenvedon vuosi-kuukausi
        print(vuosi, kuukausi)

if __name__ == "__main__":
    main()