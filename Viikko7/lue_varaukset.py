# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

'''käytän sanakirjaa (dict) tässä tehtävässä'''

from datetime import datetime
from typing import List, Dict, Any

def muunna_varaustiedot(varaus: List[str]) -> Dict[str, Any]:
    """
    Muuntaa listan (pituus 11) dictiksi oikeilla tyypeillä.
    Odotettu järjestys:
      0 id, 1 nimi, 2 email, 3 puhelin, 4 pvm, 5 klo,
      6 kesto, 7 hinta, 8 vahvistettu, 9 tila, 10 luotu
    """
    if len(varaus) != 11:
        raise ValueError(f"Kenttiä {len(varaus)}, odotettiin 11: {varaus!r}") # tarkistaa alkioiden määrän

    # Siistitään mahdolliset välilyönnit
    varaus = [x.strip() for x in varaus]

    # Muodostetaan sanakirja
    return {
        "varausId": int(varaus[0]),
        "nimi": varaus[1],
        "email": varaus[2],
        "puhelin": varaus[3],
        "varauksenPvm": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "varauksenKlo": datetime.strptime(varaus[5], "%H:%M").time(),
        "varauksenKesto": int(varaus[6]),
        # Hyväksy myös pilkku desimaalierottimena
        "hinta": float(varaus[7].replace(",", ".")),
        # Tee bool-parse hieman joustavammaksi:
        "varausVahvistettu": varaus[8].strip().lower() in ("true", "1", "yes", "y", "on"),
        "varattuTila": varaus[9],
        "varausLuotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"),
    }

def hae_varaukset(varaustiedosto: str) -> Dict[int, Dict[str, Any]]:
    varaukset: Dict[int, Dict[str, Any]] = {}
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi_numero, raw in enumerate(f, start=1):
            rivi = raw.strip()
            if not rivi or rivi.startswith("#"):
                continue  # ohitetaan tyhjät/kommentit
            osat = [o.strip() for o in rivi.split("|")]
            try:
                varaus = muunna_varaustiedot(osat)
            except Exception as e:
                raise ValueError(f"Virhe rivillä {rivi_numero}: {e}") from e # etsii virheen ja kertoo missä se on

            key = varaus["varausId"]
            if key in varaukset:
                # Voit halutessasi nostaa virheen duplikaateista:
                # raise ValueError(f"Duplikaatti varausId {key} rivillä {rivi_numero}")
                print(f"Varoitus: duplikaatti varausId {key} rivillä {rivi_numero}, korvataan aiempi.")
            varaukset[key] = varaus
    return varaukset

def vahvistetut_varaukset(varaukset: Dict[int, Dict[str, Any]]) -> None:
    for v in varaukset.values():
        if v["varausVahvistettu"]:
            print(f"- {v['nimi']}, {v['varattuTila']}, {v['varauksenPvm'].strftime('%d.%m.%Y')} klo {v['varauksenKlo'].strftime('%H.%M')}")
    print()

def pitkat_varaukset(varaukset: Dict[int, Dict[str, Any]]) -> None:
    for v in varaukset.values():
        if v["varauksenKesto"] >= 3:
            print(f"- {v['nimi']}, {v['varauksenPvm'].strftime('%d.%m.%Y')} klo {v['varauksenKlo'].strftime('%H.%M')}, kesto {v['varauksenKesto']} h, {v['varattuTila']}")
    print()


def varausten_vahvistusstatus(varaukset: Dict[int, Dict[str, Any]]) -> None:
    for v in varaukset.values():
        status = "Vahvistettu" if v["varausVahvistettu"] else "EI vahvistettu"
        print(f"{v['nimi']} → {status}")
    print()


def varausten_lkm(varaukset: Dict[int, Dict[str, Any]]) -> None:
    vahvistetut = sum(1 for v in varaukset.values() if v["varausVahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: Dict[int, Dict[str, Any]]) -> None:
    tulot = sum(v["varauksenKesto"] * v["hinta"] for v in varaukset.values() if v["varausVahvistettu"])
    print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")
    print()


def main() -> None:
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()