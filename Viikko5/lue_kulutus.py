def muunna_tiedot(KulutusTuotanto: list) -> list:


    muutettu_tieto = []
    muutettu_tieto.append(int(KulutusTuotanto[0]))  # Vuosi
    
    """ muutettu_varaus.append(str(varaus[1]))
    muutettu_varaus.append(str(varaus[2]))
    muutettu_varaus.append(str(varaus[3]))
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())
    muutettu_varaus.append(int(varaus[6]))    
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8] == "True")
    muutettu_varaus.append(str(varaus[9]))
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S")) """
    
    return muutettu_tieto


def lue_data(tiedoston_nimi: str) -> list:
    KulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Ohitetaan otsikkorivi
        for KulutusTuotantoTieto in f:
            KulutusTuotantoTieto = KulutusTuotantoTieto.strip()
            KulutusTuotantoTietoSarakkeet = KulutusTuotantoTieto.split(",")
            KulutusTuotantoTiedot.append(muunna_tiedot(KulutusTuotantoTietoSarakkeet))
    
    return KulutusTuotantoTiedot

def main():

    KulutusTuotantotiedot = lue_data("viikko42.csv")
    #print(lue_data("viikko42.csv"))
    print(lue_data("viikko42.csv")[0])  # Tulostaa toisen rivin (ensimmäinen data rivi)
    print(lue_data("viikko42.csv")[1])  # Tulostaa toisen rivin (ensimmäinen data rivi)

if __name__ == "__main__":
    main()